#!/usr/bin/env python3
import configparser
from csv import DictWriter
import json
from os import listdir
import sys

# want to return a dict (lowercase : FileName.json) to recursively get nested
#   methods and properties.
def getAllFileDict(api_data):
    master_API_dict = {}

    for entry in listdir(api_data):
        key = str(entry.split(".")[0])
        master_API_dict[key] = entry

    return master_API_dict


# import all data from specified filename
def importData(filename):

    # read in JSON data
    with open(filename, encoding='utf-8') as data_file:
        data = json.loads(data_file.read())

    return data['api']


# once imported data from file, extract the desired properties
def extractProperties(json_data):

    # this only works if guaranteed that json file has one key under 'api'
    interface_name = list(json_data.keys())[0]
    property_list = list(json_data[interface_name].keys())
    if "__compat" in property_list:
        property_list.remove("__compat")

    return str(interface_name), property_list


def recursivelyGetProperties(current_interface, res_dict, master_API_dict):

    # import data from file
    data = importData(current_interface)

    # extract interface name and its associated property list
    interface_name, property_list = extractProperties(data)

    # add entries into the output
    res_dict[interface_name] = property_list

    # iterate over all properties, search if they exist in the master API list
    for entry in property_list:

        # (all keys within res_dict and master_API_dict are lowercase)
        entry = str.lower(entry)
        if (entry in master_API_dict):

            # if they exist, make sure they aren't already in the results dict
            if (entry not in res_dict.keys()):

                # take result, create new seed and recursively fill res_dict
                new_seed = sys.argv[2] + master_API_dict[entry]
                res_dict = recursivelyGetProperties(new_seed, res_dict, \
                        master_API_dict)
    return res_dict

def main():
    config = configparser.ConfigParser()
    config.read('config.ini')

    seed_apis = config['DEFAULT']['seed']
    api_data = config['DEFAULT']['api_data']
    output = config['DEFAULT']['output']

    # init empty dict to store all results
    res_dict = {}

    # read in all available files to recurse over
    master_API_dict = getAllFileDict(api_data)

    # open seed file
    file_list = open(seed_apis).read().splitlines()

    # iterate over the list of specified files
    for entry in file_list:

        # generate a nice filename
        file_location = api_data + entry
        res_dict = recursivelyGetProperties(file_location, res_dict, \
                master_API_dict)

    # dump all results to a file
    with open(output, 'w') as fp:
        json.dump(res_dict, fp, indent=4)

if __name__ == '__main__':
    main();
