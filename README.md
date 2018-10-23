## Overscripted Web: Data Analysis in the Open

The Systems Research Group (SRG) at Mozilla have created and open sourced a data set of publicly available information that was collected by a November 2017 Web crawl. We want to empower the community to explore the unseen or otherwise not obvious series of JavaScript execution events that are triggered once a user visits a webpage, and all the first- and third-party events that are set in motion when people retrieve content.
Some preliminary insights already uncovered from this data are illustrated in this [blog post](https://medium.com/firefox-context-graph/overscripted-digging-into-javascript-execution-at-scale-2ed508f21862). 
Ongoing analyses can be tracked [here](https://github.com/mozilla/Overscripted-Data-Analysis-Challenge/tree/master/analyses)

### Technical criteria for submitting an analysis:
- Analyses should be performed in Python using the [jupyter scientific notebook](https://jupyter-notebook.readthedocs.io/en/stable/) format and executing in this [environment](https://github.com/mozilla/Overscripted-Data-Analysis-Challenge/blob/master/analyses/environment.yaml). 
- Analysis can be submitted by filing a [Pull Request](https://help.github.com/articles/using-pull-requests) against __this__[ repository](https://github.com/mozilla/Overscripted-Data-Analysis-Challenge) with the analysis formatted as an *.ipynb file in the /analyses/ folder. 
  - Environment can be confugured locally by calling `conda env create -f  environment.yaml`
- Only *.ipynb format entries submitted via a pull request to the /analyses/ folder will be considered. Notebooks must be well documented and run on the [environment](https://github.com/mozilla/Overscripted-Data-Analysis-Challenge/blob/master/analyses/environment.yaml) described. Any entries not meeting these criteria will not be considered and no review will be carried out for error-generating code.
- Any additional code submitted will not be considered. The *.ipynb notebook should be a self contained analysis.

### Accessing the Data
Each of the links below links to a bz2 zipped portion of the total dataset. A small sample of the data is available in `safe_dataset.sample.tar.bz2` to get a feel for the content without commiting to the full download.
- [https://public-data.telemetry.mozilla.org/bigcrawl/safe_dataset.sample.tar.bz2](https://public-data.telemetry.mozilla.org/bigcrawl/safe_dataset.sample.tar.bz2)

Unzipped the full parquet data will be approximately 70Gb. Each (compressed) chunk dataset is around 9GB. `SHA256SUMS` contains the checksums for all datasets including the sample.
- [https://public-data.telemetry.mozilla.org/bigcrawl/safe_dataset.0.tar.bz2](https://public-data.telemetry.mozilla.org/bigcrawl/safe_dataset.0.tar.bz2)
- [https://public-data.telemetry.mozilla.org/bigcrawl/safe_dataset.1.tar.bz2](https://public-data.telemetry.mozilla.org/bigcrawl/safe_dataset.1.tar.bz2)
- [https://public-data.telemetry.mozilla.org/bigcrawl/safe_dataset.2.tar.bz2](https://public-data.telemetry.mozilla.org/bigcrawl/safe_dataset.2.tar.bz2)
- [https://public-data.telemetry.mozilla.org/bigcrawl/safe_dataset.3.tar.bz2](https://public-data.telemetry.mozilla.org/bigcrawl/safe_dataset.3.tar.bz2)
- [https://public-data.telemetry.mozilla.org/bigcrawl/SHA256SUMS](https://public-data.telemetry.mozilla.org/bigcrawl/SHA256SUMS)
