# Ad Blocker Usage Detection Report
### Summary
Ad blocker usage can be detected by checking the state of one of your ad scripts.  It is frequently used to restrict functionality for ad blocking users or as a bit of information in user fingerprinting.


### Detection
#### In Literature
In _Measuring and Disrupting Anti-Adblockers Using
Differential Execution Analysis_ anti adblockers were detected on 30.5% of the Alexa top-10K websites. This is trending upwards significantly as in May 2016 only 6.7% were detected using anti-adblock software.

#### In The Overscripted Dataset
Anti-adblock behaviour could not be detected in the dataset.

#### What else would we need to detect it?
Adblock detection can be done by running two crawls, one with adblock one without, and comparing the behaviour differences. This would allow the overscripted set to detect behaviour differences as well as frequency.
