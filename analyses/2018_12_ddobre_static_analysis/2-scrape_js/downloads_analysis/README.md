# JavaScript Redundancy Analysis

The purpose of these scripts are to analyze the difference between the uncleansed `script_url`s from the full dataset and their parsed counterparts. The parsed 'condensed dataset' essentially omits any queries that were included in the `script_url`, condensing the number of entries from over a million to less than 200000.

`extract_hashes_from_full_dataset.py` generates a dictionary of hashes for every file (with `utf-8` encoding) in the specified directory. It is far too expensive to try to do this whole process in one step - filesystems are not fond of having over 800000 files in one directory. The pickled output is used in the next step.
 
`compare_condensed_with_full.py` uses the data from the above script and iterates over the specified condensed dataset, generating a final pickled output of a pandas dataframe with a schema of `['parent_url', 'url', 'hash']`, allowing the comparison between hashes sharing the same base URL.

`explore_downloads.ipynb` is a jupyter-notebook containing a brief analysis on the redundancy of the JS files when making requests with queries.

Note: for a small section on the HTTP status response, you will require `js_status.csv`, which is the output of Pt.2's download script dumped into a text file. This stores the URLs and their HTTP response status. This is not necessary for the rest of the analysis so you can remove the associated code to this.

