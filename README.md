## Overscripted Web: Data Analysis in the Open

The Systems Research Group (SRG) at Mozilla have created and open sourced a data set of publicly available information that was collected by a November 2017 Web crawl. We want to empower the community to explore the unseen or otherwise not obvious series of JavaScript execution events that are triggered once a user visits a webpage, and all the first- and third-party events that are set in motion when people retrieve content.
Some preliminary insights already uncovered from this data are illustrated in this [blog post](https://medium.com/firefox-context-graph/overscripted-digging-into-javascript-execution-at-scale-2ed508f21862). 
Ongoing analyses can be tracked [here](https://github.com/mozilla/overscripted/tree/master/analyses)

The crawl data hosted here was collected using [OpenWPM](https://github.com/mozilla/OpenWPM), which is developed and maintained by the Mozilla Security Engineering team.

### Submitting an analysis:
- Analyses should be performed in Python using the [jupyter scientific notebook](https://jupyter-notebook.readthedocs.io/en/stable/) format and executing in this [environment](https://github.com/mozilla/overscripted/blob/master/analyses/environment.yaml). 
- Analysis can be submitted by filing a [Pull Request](https://help.github.com/articles/using-pull-requests) against this repository with the analysis formatted as an *.ipynb file or folder in the /analyses/ folder. 
- Set-up instructions are provided here: https://github.com/mozilla/overscripted/blob/master/analyses/README.md
- Notebooks must be well documented and run on the [environment](https://github.com/mozilla/overscripted/blob/master/analyses/environment.yaml) described. If additional installations are needed these should be documented.
- Files and folders should have the format `yyyy_mm_username__short-title` - the analyses directory contains examples already if this is not clear.
- PRs altering or updating an existing analysis will not be accepted unless they are tweaking formatting / small errors to facilitate that notebook running. If you wish to continue / build-on someone else's existing analysis start your own analysis folder / file, cite their work, and then proceed with your extension.

### Accessing the Data
Each of the links below links to a bz2 zipped portion of the total dataset. 

A small sample of the data is available in `safe_dataset.sample.tar.bz2` to get a feel for the content without commiting to the full download.
- [https://public-data.telemetry.mozilla.org/bigcrawl/safe_dataset.sample.tar.bz2](https://public-data.telemetry.mozilla.org/bigcrawl/safe_dataset.sample.tar.bz2)

Three samples that are large enough to meaningful analysis of the dataset are
also available as the full dataset is very large. More details about the
samples are available in [data_prep/Sample Review.ipynb](https://github.com/mozilla/overscripted/blob/master/data_prep/Sample%20Review.ipynb)
- https://public-data.telemetry.mozilla.org/bigcrawl/sample_10percent_value_1000_only.parquet.tar.bz2 - 900MB download / 1.3GB on disk
- https://public-data.telemetry.mozilla.org/bigcrawl/sample_10percent.parquet.tar.bz2 - 3.7GB download / 7.4GB on disk
- https://public-data.telemetry.mozilla.org/bigcrawl/value_1000_only.parquet.tar.bz2 - 9.1GB download / 15GB on disk

The full dataset. Unzipped the full parquet data will be approximately 70GB. Each (compressed) chunk dataset is around 9GB. `SHA256SUMS` contains the checksums for all datasets including the sample.
- [https://public-data.telemetry.mozilla.org/bigcrawl/safe_dataset.0.tar.bz2](https://public-data.telemetry.mozilla.org/bigcrawl/safe_dataset.0.tar.bz2)
- [https://public-data.telemetry.mozilla.org/bigcrawl/safe_dataset.1.tar.bz2](https://public-data.telemetry.mozilla.org/bigcrawl/safe_dataset.1.tar.bz2)
- [https://public-data.telemetry.mozilla.org/bigcrawl/safe_dataset.2.tar.bz2](https://public-data.telemetry.mozilla.org/bigcrawl/safe_dataset.2.tar.bz2)
- [https://public-data.telemetry.mozilla.org/bigcrawl/safe_dataset.3.tar.bz2](https://public-data.telemetry.mozilla.org/bigcrawl/safe_dataset.3.tar.bz2)
- [https://public-data.telemetry.mozilla.org/bigcrawl/SHA256SUMS](https://public-data.telemetry.mozilla.org/bigcrawl/SHA256SUMS)

Refer [hello_world.ipynb](https://github.com/mozilla/overscripted/blob/master/analyses/hello_world.ipynb) to load and have a quick look at the data with pandas, dask and spark.

### New Contributor Tips

- Make contributions with respect to any of your learnings, be it by reading related research papers or through your interaction with the community on gitter and submitting a Pull Request (PR) to the repository. You can submit the PR to the README on the main page or the analysis folder README.

- This is not a one issue per person repo. All the questions are very open ended and different people may find very different and complementary things when looking at a question.

- Use a reaction emoji to acknowledge a comment rather than writing a comment like "sure" - helps to keep things clean - but the contributor can still let folks know that they saw a comment.

- You can ask for help and discuss your ideas on gitter. Click [here](https://gitter.im/overscripted-discuss/community) to join !

- When you open an issue and work on a Pull Request relating to the same, add "WIP" in the title of the PR. "WIP" is work in progress. When your PR is ready for review remove the WIP tag. You can also request feedback on specific things while it's still a WIP.

- Please reference your issues on a PR so that they link and autoclose. Refer to [this](https://help.github.com/en/articles/closing-issues-using-keywords)

- If your OS is Ubuntu and you have trouble installing spark with conda. Refer to this [link](https://datawookie.netlify.com/blog/2017/07/installing-spark-on-ubuntu/).

- The dataset is very large. Even the subsets of the dataset are unlikely to fit into memory. Working with this dataset will typically require using Dask (http://dask.pydata.org/), Spark (http://spark.apache.org/) or similar tools to enable parallelized / out-of-core / distributed processing.

### Glossary
- [Fingerprinting](https://en.wikipedia.org/wiki/Device_fingerprint) is the process of creating a unique identifier based off of some characteristics of your hardware, operating  system and browser. 
- TLD means Top-level Domain. You can read up more about it [here.](https://en.wikipedia.org/wiki/Top-level_domain) 
- [User Agent](https://en.wikipedia.org/wiki/User_agent) (UA), is a string that helps identify which browser is being used, what version, and on which operating system. 
- [Web Crawler](https://en.wikipedia.org/wiki/Web_crawler)- It is a program or automated script which browses the World Wide   Web in a methodical, automated manner.



### Resources

- Please refer the [reading list](https://github.com/mozilla/overscripted/wiki/Reading-List-(WIP)) for additional references and information.

- [This](https://github.com/brandon-rhodes/pycon-pandas-tutorial) is a great tutorial to learn Pandas.

- [Tutorial](https://www.youtube.com/watch?v=HW29067qVWk) on Jupyter Notebook.

- We have used dask in some of our Jupyter notebooks. Dask gives you a pandas-like API but lets you work on data that is too big to fit in memory. Dask can be used on a single machine or a cluster. Most analyses done for this project were done on a single machine. Please start by reviewing the [docs](https://dask.org/) to learn more about it.

- [This](https://github.com/aSquare14/Git-Cheat-Sheet) will help you get started with GIT. For visual thinkers this [tutorial](https://www.youtube.com/playlist?list=PL6gx4Cwl9DGAKWClAD_iKpNC0bGHxGhcx) can be a good start.

- Other Dask resources: [overview](https://www.youtube.com/watch?v=ods97a5Pzw0) video and [cheatsheet](https://dask.pydata.org/en/latest/_downloads/daskcheatsheet.pdf).

- [Apache Spark](https://spark.apache.org/docs/latest/api/python/pyspark.html) is an open source parallel processing framework for running large-scale data analytics applications across clustered computers. It can handle both batch and real-time analytics and data processing workloads. We use [findspark](https://github.com/minrk/findspark) to set up spark. You can learn more about it [here](https://github.com/apache/spark )

