import configparser
from os import path
import sys
from slugify import slugify
from pyspark.sql import SparkSession, functions, types

# Safety for spark stuff
spark = SparkSession.builder.appName('URL extractor').getOrCreate()
assert sys.version_info >= (3, 4) # make sure we have Python 3.4+
assert spark.version >= '2.1' # make sure we have Spark 2.1+

# UDF to generate a text file from the script URL
def shorten_name(url_name):
    # Strip out 'http', 'https', '/', and '.js'
    shortened_url = url_name.replace(
                                'https://', ''
                            ).replace(
                                'http://', ''
                            ).replace(
                                '/', '_'
                            ).replace(
                                '.js', ''
                            )

    # Shorten url to 250 characters (max file system can support)
    shortened_url = slugify(shortened_url)[:250]

    # Specify the suffix for each downloaded file
    suffix = '.txt'

    # Final output
    file_name = shortened_url + suffix
    return file_name

def main():

    # Specify target directory
    config = configparser.ConfigParser()
    config.read('config.ini')

    datatop = config['DEFAULT']['datatop']
    parquet_dataset = path.join(datatop,config['DEFAULT']['parquet_dataset'])
    output_dir = path.join(datatop,config['DEFAULT']['output_dir'])

    # Read in dataset, selecting the 'script_url' column and filter duplicates
    data = spark.read.parquet(parquet_dataset).select('script_url').distinct()

    # Split the string on reserved url characters to get canonical url
    data = data.withColumn(
                    "parsed_url",
                    functions.split("script_url", "[\?\#\,\;]")[0]
                ).distinct()

    # Only keep urls that are actually .js files
    data = data.filter(
                data["parsed_url"].rlike("\.js$")
            ).dropDuplicates(["parsed_url"])

    # User Defined Function to convert script URL to a filename usable by ext4
    shorten_udf = functions.udf(shorten_name, returnType=types.StringType())

    # Apply the UDF over the whole list to generate a new column 'filename'
    data = data.withColumn(
                'filename',
                shorten_udf(data.parsed_url)
            ).sort('filename')

    # Save the data to parquet files
    data.write.parquet(output_dir)
    config = configparser.ConfigParser()
    config.read('config.ini')


if __name__ == '__main__':
    main();
