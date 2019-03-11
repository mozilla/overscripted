#!/usr/bin/env python3
import requests
import sys

url = sys.argv[1]

TIMEOUT = 2
OUT_FILENAME = "downloaded.js"

try:
    response = requests.get(url, timeout=TIMEOUT)

    if response.status_code == 200:
        print("File found - writing contents to {}".format(OUT_FILENAME))

        with open(OUT_FILENAME, "w") as source_file:
            source_file.write(response.text)

    else:
        print("Error! Status code: {}".format(response.status_code))

except request.exceptions.RequestException as e:
    print("Exception")
    print(e)
