#! /usr/bin/env python3
import sys
import hashlib
import glob
from pathlib import Path
from os import path
import pickle

STORAGE_DIR = "/mnt/Data/UCOSP_DATA"

ALL_FILES = path.join(STORAGE_DIR, ("1st_batch_js_source_files" + "/*"))

OUTPUT_FILE = "full_data.pickle"

OUTPUT_FILE_FAILS = "fails.pickle"

# Generating new dataframe
def get_hash_from_file(filename):
    sha1 = hashlib.sha1()
    with open(filename, "r") as f:
        data = f.read()
        sha1.update(data.encode("utf-8"))
    return sha1.hexdigest()

# Get file list
print("Retrieving list from: '{}'".format(ALL_FILES))
total_file_list = list(glob.glob(ALL_FILES))
total_num_files = len(total_file_list)
print("Retrieved list of {} files.\n".format(total_num_files))

output_dict = {}
output_fails = []
counter = 0
fails = 0

# Iterate over entire file list
for filename in total_file_list:
    if counter % 20000 == 0:
        print(80 * "#" + "\n")
        print("{}/{}".format(counter, total_num_files))
        print(80 * "#" + "\n")

    raw_filename = filename.split("/")[-1]
    try:
        file_hash = get_hash_from_file(filename)
    except UnicodeDecodeError as e:
        print("Bad type:\n{}".format(e))
        fails += 1
        output_fails.append(raw_filename)
        continue

    output_dict.update({raw_filename: file_hash})
    counter += 1

print(
    "{}/{}\n\nDONE... Now pickling data to: '{}'".format(
        counter, total_num_files, OUTPUT_FILE
    )
)

with open(OUTPUT_FILE, "wb") as f:
    # Pickle the 'data' dictionary using the highest protocol available.
    pickle.dump(output_dict, f, pickle.HIGHEST_PROTOCOL)

# Store fails for a later time
with open(OUTPUT_FILE_FAILS, "wb") as f:
    pickle.dump(output_fails, f)

print("DONE\nFinal stats:\nSuccess:\t{}\nFails:\t{}".format(counter, fails))
