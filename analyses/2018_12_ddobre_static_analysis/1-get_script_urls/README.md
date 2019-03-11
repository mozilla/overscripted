# Extract script URLs from dataset
_Note, this section uses pySpark_

## 1) Setup Spark:

1) You must have Open JDK 8. Install via `$ sudo apt-get install openjdk-8-jdk` if you don't have this installed (check if `/usr/lib/jvm/java-8-openjdk-amd64/` exists).

2) Download the latest version of [Spark](https://spark.apache.org/downloads.html) (prebuilt for Apache Hadoop 2.7 and later), and unpack the tar to a directory of your choosing.

3) Set some environment variables:
```
$ export PYSPARK_PYTHON=python3
$ export PATH=${PATH}:/path/to/spark-<version>-bin-hadoop2.7/bin
$ export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64/ 
```

To run any of the pyspark scripts on their own, you can run
```
$ spark-submit sparkscript.py
```

**Note: you may need to increase spark driver memory.**
In `<spark_dir>/conf/spark-defaults.conf`, add the line `spark.driver.memory 15g`, or whatever is acceptable for your system.


## 2) Running the scripts:

Replace the appropriate directories in `config.ini` for your system. You will need the [Full Mozilla Overscripted Dataset](https://github.com/mozilla/Overscripted-Data-Analysis-Challenge). 

Ensuring spark is set up as in pt. 1, run:
```
$ spark-submit generate_url_list_spark.py
```

To test individual user specified urls, you can place urls in `test_urls.csv` and run `$ spark-submit test_generate_url_list_spark.py`. This will output `parsed_test_urls.csv` using the exact same process as on the full dataset for easy debugging and sanity checks.

A jupyter notebook with barebones loading and displaying of the data to make exploring the results easier.

