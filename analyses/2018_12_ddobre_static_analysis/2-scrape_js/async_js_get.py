#!/usr/bin/env python3
#
# Original code: Cristian Garcia, Sep 21 '18
#       https://medium.com/@cgarciae/making-an-infinite-number-of-requests-with-
#               python-aiohttp-pypeln-3a552b97dc95
#
# Script adapted by David Dobre Nov 20 '18:
#       Added parquet loading, iteration over dataframes, and content saving
#
# NOTE: You may need to increase the ulimit (3000 worked for me):
#
#           $ ulimit -n 3000
#
################################################################################

from aiohttp import ClientError, ClientSession, TCPConnector
import asyncio
import configparser
import glob
import os, os.path
import pandas as pd
import ssl
import sys

from pathlib import Path
from pypeln import asyncio_task as aio

##### Specify directories and parameters
config = configparser.ConfigParser()
config.read('config.ini')

# Top directory
datatop = config['DEFAULT']['datatop']

# Input directory
url_list = os.path.join(datatop, config['DEFAULT']['url_list'])

# Output directory
output_dir = os.path.join(datatop, config['DEFAULT']['output_dir'])

# Max number of workers
limit = config['DEFAULT'].getint('limit')

print(datatop)
print(url_list)
print(output_dir)
print(limit)

# Not sure what this monkey business does
ssl.match_hostname = lambda cert, hostname: True

##### Load in dataset ##########################################################
parquet_dir = Path(url_list)
input_data = pd.concat(
    pd.read_parquet(parquet_file)
    for parquet_file in parquet_dir.glob('*.parquet')
)

# Check for existing files in output directory
existing_files = [os.path.basename(x) for x in glob.glob(output_dir + "*.txt")]

# Remove those from the "to request" list as they're already downloaded
input_data = input_data[~input_data['filename'].isin(existing_files)]

# Append filename to the output folder and get the raw string value
input_data['filename'] = output_dir + input_data['filename']
input_data = input_data.values

print("url,status,")

##### Async fetch ##############################################################
async def fetch(data, session):

    url = data[1]
    filename = data[2]

    try:
        async with session.get(url, timeout=2) as response:
            output = await response.read()
            print("{},{},".format(url, response.status))

            if (response.status == 200 and output):
                with open(filename, "wb") as source_file:
                    source_file.write(output)
                return output

            return response.status

    # Catch exceptions
    except ClientError as e:
        print("{},{},".format(url, e))
        return e

    except asyncio.TimeoutError as e:
        print("{},{},".format(url, e))
        return erb

    except ssl.CertificateError as e:
        print("{},{},".format(url, e))
        return e

    except ssl.SSLError as e:
        print("{},{},".format(url, e))
        return e

    except ValueError as e:
        print("{},{},".format(url, e))
        return e

    except TimeoutError as e:
        print("{},{},".format(url, e))
        return e

    except concurrent.futures._base.TimeoutError as e:
        print("{},{},".format(url, e))
        return e


##### Iterate over each list entry #############################################
aio.each(
    fetch,              # worker function
    input_data,         # input arguments
    workers = limit,    # max number of workers
    on_start = lambda: ClientSession(connector=TCPConnector(limit=None)),
    on_done = lambda _status, session: session.close(),
    run = True,
)
