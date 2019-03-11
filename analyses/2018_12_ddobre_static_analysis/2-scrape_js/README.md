# Asynchronous Batch Downloading of JavaScript files

`async_js_get.py` iterates over the parquet files generated in part 1 to asynchronously download all of the files. The script first scans your specified output directory to skip over the already downloaded files. No arguments are needed, just ensure that you satisfied all of the requirements specified in `requirements.txt`. Run with:
```
$ ./async_js_get.py > js_status.csv
```
This saves the status responses for some analysis if so desired later. Note that the error codes may have some characters invalidating the schema (namely extra commas).

You may run into some system configuration issues; you may need to increase the ulimit (3000 worked for me):

```
$ ulimit -n 3000
```
