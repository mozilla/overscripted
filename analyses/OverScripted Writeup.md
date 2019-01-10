**[Online Tracking: An OverScripted Measurement and
Analysis]{.underline}**

**The Overview**

Fingerprinting on the internet is getting worse. More sites and more
advertising companies are tracking you around the internet without your
consent than before.

+-----------+-----------+-----------+-----------+-----------+-----------+
|           | Web Census            | OverScripted          |           |
|           | (January, 2016)       | (December, 2017)      |           |
|           |                       |                       |           |
|           |                       |                       |           |
|           |                       |                       |           |
|           |                       |                       |           |
+===========+===========+===========+===========+===========+===========+
|           | \# of     | \% of     | \# of     | \% of     | \% Change |
|           | Sites     | Total     | Sites     | Total     | in % of   |
|           | (Location | Sites     | (Location | Sites     | Sites     |
|           | s)        |           | s)        |           |           |
+-----------+-----------+-----------+-----------+-----------+-----------+
| Canvas    | 14,371    | 1.44%     | 60,141    | 2.92%     | 202%      |
| Fingerpri |           |           |           |           |           |
| nting     |           |           |           |           |           |
+-----------+-----------+-----------+-----------+-----------+-----------+
| Canvas    | 3,250     | 0.33%     | 1,900     | 0.09%     | -367%     |
| Font      |           |           |           |           |           |
| Fingerpri |           |           |           |           |           |
| nting     |           |           |           |           |           |
+-----------+-----------+-----------+-----------+-----------+-----------+
| WebRTC    | 715       | 0.07%     | 11,539\*  | 0.56%     | 800%      |
| Fingerpri |           |           |           |           |           |
| nting     |           |           |           |           |           |
+-----------+-----------+-----------+-----------+-----------+-----------+
| AudioCont | N/A\*\*   | N/A\*\*   | 1,717     | 0.08%     | N/A       |
| ext       |           |           |           |           |           |
| Fingerpri |           |           |           |           |           |
| nting     |           |           |           |           |           |
+-----------+-----------+-----------+-----------+-----------+-----------+

Note: Web Census data is from "Online Tracking: A 1-million-site
Measurement and Analysis" by S. Englehardt and A. Narayanan

\* This is just the number of sites using WebRTC fingerprinting with
calls to onicecandidate, createDataChannel and createOffer; see the
section on WebRTC fingerprinting for more details.

\*\* The number of sites using AudioContext fingerprinting was not
provided in the web census data.

**The Background**

Back in October 2017 as part of an earlier iteration of the
Undergraduate Capstone Open-Source Project (UCOSP), a group of Canadian
university students and Mozilla staff members forked the OpenWPM crawler
repo. The goal of this project was to track the execution of JavaScript
across the web. The crawler visited just under a million webpages and
captured the JavaScript execution trace on the webpage and within any
iFrame elements. This produced a list of all browser APIs that a webpage
called on load, both to render content and potentially track the user.

This project continued in January 2018 with another set of UCOSP
students who performed initial exploratory work. They looked for
instances of session replay---where a website tracks users' interactions
with the page---by cross-referencing the OverScripted dataset with the
Princeton WebTAP project list. They also examined the prevalence of
dynamically created function calls which could open up the user to
cross-site scripting attacks. Finally, cryptojacking is a relatively new
usage of malicious JavaScript that was found in the dataset. Full
details of the analysis can be found [here]
(https://hacks.mozilla.org/2018/06/overscripted-digging-into-javascript-execution-at-scale/).

**The Problem**

Given the previous work, what we decided to look at next was
fingerprinting. Fingerprinting is the process of creating a unique
identifier based off of some characteristics of your hardware, operating
system and browser. The basic idea behind it is that JavaScript can
access a bunch of different APIs that your browser has implemented. When
used correctly, these allow webpages to be rendered properly. However,
those APIs can also be abused, for example through the processing of an
audio signal generated with an OscillatorNode to create a unique
identifier. This allows for third-party trackers to track you around the
internet without cookies or consent as the fingerprint would be unique
to your specific device. Further details on fingerprinting can be found
in "The web never forgets: Persistent tracking mechanisms in the wild"
by G. Acar et al. and "Online Tracking: A 1-million-site Measurement and
Analysis" by S. Englehardt and A. Narayanan.

This is obviously a problem. At least with a cookie, a user is given a
choice about whether to accept it in the first place and when they want
to delete it, even if those settings can be hidden deep in the web
browser. With fingerprinting, there is no choice and it is very hard to
protect against as you would need to spoof multiple bits of information.
However, before attempting to come up with a solution, we need to
determine how prevalent it is in the first place. That is where
Englehardt and Narayanan's analysis along with the OverScripted dataset
come in.

**The Process**

Thankfully, in order to determine the prevalence of tracking, we did not
need to reinvent the wheel. The heuristics that Englehardt and Narayanan
used to determine if a script utilizes fingerprinting are detailed in
their paper "Online Tracking: A 1-million-site Measurement and
Analysis." These heuristics form the base of our analysis. Our
goal was to reimplement the heuristics described for Canvas fingerprintng, 
Canvas Font fingerprinting, WebRTC fingerprinting and AudioContext 
fingerprinting and run them against the OverScripted dataset. This would give 
us an approximation of how much fingerprinting is going on in the wild close
to two years after Englehardt and Narayanan's original study. Their work
would also be a good ground truth to test our results for sanity
against. Before getting into the details, a quick note about the Battery API
fingerprinting mentioned in section 6.5 of Englehardt and Narayanan's
work: the API required was removed in Firefox 52 which shipped on on
March 6, 2017. Since the OverScripted dataset was collected at the end
of 2017, this API would not have been available and so no Battery API
fingerprinting would have been possible.

**The Data**

In order to have context for how many fingerprinting scripts were found,
we need to know same basic information about the dataset itself. Within
the OverScripted dataset, there were 1,253,168 unique script urls
called. These are JavaScript files which were then executed by the web
browser. These are not necessarily 1,253,168 unique scripts though; if
the script url that was called had any unique identifier passed along in
the url that script would show up multiple times in the dataset. Another
piece of information we need to know is where the scripts are being
called from, i.e. the location. There are 2,059,503 unique locations
within the dataset. Putting those two pieces of information together
results in a tuple of (script url, location) for each script called from
each webpage. There are 6,064,923 unique tuples representing 6,064,923
distinct script references among page loads. Finally, we were also able
to gather the specific parameters passed to a JavaScript function.

**Canvas Fingerprinting**

Canvas fingerprinting utilizes the HTML Canvas API to isolate
differences in in font rendering, smoothing, anti-aliasing and other
device functionality that cause images to be rendered differently. These
differences, taken together, allow for a device to be uniquely
fingerprinted. Englehardt and Narayanan isolate 4 different heuristics
that, when combined, identify a script that is using Canvas
fingerprinting. Those heuristics are:

-   The canvas element's height and width properties must not be set
    > below 16 px.

-   Text must be written to canvas with least two colours or at least 10
    > distinct characters.

-   The script should not call the save, restore, or addEventListener
    > methods of the rendering context.

-   The script extracts an image with toDataURL or with a single call to
    > getImageData that specifies an area with a minimum size of 16px ×
    > 16px.

(Source: Steven Englehardt and Arvind Narayanan, \"Online tracking: A
1-million-site measurement and analysis," pg. 12)

In their analysis, Englehardt and Narayanan found Canvas fingerprinting
on 14,371 sites (1.44% of the total). In our analysis we found 60,141
sites using Canvas fingerprinting representing 2.92% of the total
locations calling 20,350 different script urls. There were also a total
of 65,263 unique tuples of (script url, location) meaning that some
sites called multiple Canvas fingerprinting scripts. This is just over a
2x increase in the number of sites using Canvas fingerprinting. Part of
that increase may come from an increase in acceptable uses such as for
fraud protection as suggested by Englehardt and Narayanan. However,
there is more awareness around this technique which probably drove some
of the increase as well. This continues to be the most prevalent kind of
fingerprinting, probably due to how long it has been around and it's
ease of use. Finally, no manual checks were done to confirm the scripts
were tracking users unlike those performed by Englehardt and Narayanan.

**Canvas Font Fingerprinting**

The HTML Canvas API can also be used to enumerate the fonts available on
a device. That information has the potential to be unique given the vast
state space of potential combinations of fonts and the number of custom
fonts available. Englehardt and Narayanan determine one criteria for
Canvas Font fingerprinting: "the script sets the font property to at
least 50 distinct, valid values and also calls the measureText method at
least 50 times on the same text string." (Source: Steven Englehardt and
Arvind Narayanan, "Online tracking: A 1-million-site measurement and
analysis," pg. 13)

In their analysis, Englehardt and Narayanan found Canvas Font
fingerprinting on 3,250 sites (0.33% of the total). In our analysis, we
found 1,900 sites using Canvas Font fingerprinting representing 0.09% of
the total locations calling 1,387 different script urls. There were also
a total of 1,900 unique tuples of (script url, location) meaning that
each site only called one Canvas Font fingerprinting script. This is
close to a 4x reduction in Canvas Font fingerprinting which could be the
result of several different factors. On one hand, greater academic
awareness of Canvas Font fingerprinting could have led to a reduction of
usage by the most prominent trackers (i.e. Google, Facebook, Twitter)
due to public backlash. Englehardt and Narayanan hypothesized that this had
occurred with Canvas fingerprinting. On the other hand, the technique
may have evolved and may be able to fingerprint a user by using less
than 50 calls to measureText or setting less than 50 distinct values.
These heuristics do lean on the conservative side and so may be
under-representing the true state of affairs. Additionally, no manual
checks were done to confirm the scripts were tracking users unlike those
performed by Englehardt and Narayanan.

**WebRTC Fingerprinting**

WebRTC allows for peer-to-peer Real Time Communication in the browser.
Certain information required to set up these connections, such as local
IP addresses, can be accessed without permission of the user. This means
that a script can access addresses from the local network interfaces.
That allows for your local IP, regardless of if you're behind a VPN or
not, to be used for tracking. This section is split up into two
different subsections as the information required for the tracking can
be accessed two different ways. The first subsection documents the
heuristics used by Englehardt and Narayanan that their results are based
off of. The second documents an alternative methodology mentioned in
footnote 14 on page 12 of Englehardt and Narayanan's work. It is
included here for breadth.

**WebRTC Fingerprinting - onicecandidate, createDataChannel,
createOffer**

The first set of heuristics involve accessing the onicecandidate,
createDataChannel and createOffer APIs. Only if a script accesses all
three of the methods can it use WebRTC fingerprinting. In their
analysis, Englehardt and Narayanan found WebRTC fingerprinting on 715
sites (0.07% of the total). In our analysis, we found 11,539 sites where
all three symbols were called representing 0.56% of the total locations
calling 1,313 different script urls. There were also a total of 12,936
unique tuples of (script url, location) meaning that some sites called
multiple WebRTC fingerprinting scripts using all the symbols. This
represents a 8x increase in the amount of WebRTC fingerprinting present
in the OverScripted dataset in the 2 years since Englehardt and
Narayanan\'s original study. Given that WebRTC was a rather new
technique then that was not widely known, it makes sense that there
would have been some increase. However, 8x as many instances is a lot
and that number may need some additional validation as there was no
manual checks performed unlike in Englehardt and Narayanan's work.
Another potential explanation is that the usage of WebRTC has increased
and as such, there are valid reasons for calling those three symbols on
today's web.

**WebRTC Fingerprinting - localDescription**

In a footnote, Englehardt and Narayanan mention that calling
localDescription would provide access to all the information needed to
carry out WebRTC fingerprinting. Therefore, we also analyzed the
prevalence of that call within the OverScripted dataset. There is a
caveat though as we did not manually confirm that these scripts were
actually carrying out fingerprinting. Englehardt and Narayanan did
perform this manual check for the heuristics listed in the previous
section. In our analysis, we found 8,815 sites where localDescription
was called representing 0.43% of the total locations calling 72
different script urls. There were also a total of 9,086 unique tuples of
(script url, location) meaning that some sites called multiple WebRTC
fingerprinting scripts using localDescription. Even though there is no
baseline to compare this number against, it seems reasonable given the
prevalence of WebRTC fingerprinting found using the previous set of
heuristics. However, the same caveat about manual validation and
potential non-malicious explanations also applies here.

**AudioContext Fingerprinting**

In the process of their analysis, Englehardt and Narayanan discovered a
new fingerprinting technique that added additional information to a
broader fingerprinting approach. The basic idea is similar to that
present in other kinds of fingerprinting, notably Canvas Font
fingerprinting. Processing the same audio signal on different machines
with different hardware and software configurations will result in
slight differences in the output signal. This output signal can then be
hashed to created a unique id that helps to fingerprint a device. The
only API call that is required for this approach is to an OscillatorNode
in order to either check for its existence or generate the output
signal.

Englehardt and Narayanan do not list all of the sites that they found
AudioContext fingerprinting on. In our analysis, we found 1,717 sites
that start an OscillatorNode representing 0.08% of the total locations
calling 534 different script urls. There were also a total of 2,082
unique tuples of (script url, location) meaning that some sites called
multiple AudioContext fingerprinting scripts. The fact that there are
this many sites using AudioContext fingerprinting, more than Canvas Font
fingerprinting, is a little surprising given that the implication from
Englehardt and Narayanan's analysis is that AudioContext fingerprinting
is rare. This could be due to a greater commercial awareness of the
benefit of AudioContext fingerprinting though after the academic
community became aware of it. Another explanation is that there may be
new legitimate uses of calling OscillatorNode that were less widespread
during Englehardt and Narayanan's crawl. Given that no absolute numbers
were provided in Englehardt and Narayanan's work, this is also an area
where some manual validation would be useful.

**Limitations**

As has been mentioned several times, there are a few limitations to both
the OverScripted dataset and the analysis that has been performed so
far. Focusing on the dataset itself, there are 2 main limitations. The
first was an issue with how the crawler recorded if the JavaScript was
running in an iFrame or not. Due to a bug in the implementation, if the
in\_iframe column is true, then the JavaScript was definitely running
inside the iFrame. However, if the in\_frame column is false, then the
code could have either been in an iFrame or not. At the moment, this
would not have affected the analysis as implemented because that column
was ignored. However, in order to get a more robust picture, JavaScript
running in an iFrame on a site should be lumped in with the other
JavaScript files that are loaded by that site as well. Right now, this
is not done since the location recorded for JavaScript running inside of
an iFrame is whatever location is loaded by the iFrame. This could
reduce the total number of sites where fingerprinting is found if a site
loaded a fingerprinting script both inside and outside of an iFrame.
Given that multiple site ran multiple scripts that performed the same
kind of fingerprinting, this could easily have occurred.

The second issue is that the web crawler only spent 10 seconds on each
page before moving on. This was determined through an ad-hoc analysis of
how long it would take all of the JavaScript on a page to execute. While
this is probably enough for the majority of sites, there is the
potential of a long tail of sites where the fingerprinting could occur
after 10 seconds has passed. There is a tradeoff here that does need to
happen however.

In terms of the analysis as presented so far, there is another
limitation. That issue, which has been mentioned several times, is the
lack of manual checks such as those performed by Englehardt and
Narayanan. These don't need to be as comprehensive but we should
followup with some spot checks in place to make sure we are on the right
track. Additionally, for the fingerprinting were there was a large
change in usage, such as with Canvas Font, there should be some manually
digging to confirm those numbers.

**Potential Extensions**

The are numerous potential avenues to pursue building upon this analysis
in the future. Out of the limitations presented above, digging deeper
into the issue of iFrames or manual validation would be valuable.
Additionally, there is the chance that new kinds of fingerprinting exist
within the dataset. A more thorough examination of the tracking scripts
that are identified could lead to new discoveries as different
fingerprinting techniques are often used in conjunction with each other.
Additionally, figuring out why some sites called multiple scripts for
the same kind of fingerprinting would be interesting. Specifically
regarding WebRTC, there needs to be a better understanding of the
overlap between the different potential WebRTC fingerprinting methods.

Moving beyond additional understanding, this analysis could be used to
train a binary classifier for whether a site is fingerprinting a user or
multi-class classifier for how is doing so. This analysis provides the
labels for a training set of which sites and which scripts fingerprint
users. Depending on the features used, which would probably include the
symbols called by the JavaScript, the classifier could perform either
static analysis as part of an analytic toolset or dynamic analysis as
part of web extension to provide insight for users.

**Final Conclusions**

While there are definitely limitations to the work done, there are
valuable insights that can be gained. The main takeaway is that
fingerprinting is here to stay. In all categories where there was a
baseline established by Englehardt and Narayanan, except for Canvas Font
fingerprinting, there has been an increase in sites using
fingerprinting. While some of these cases may be legitimate cases of
fraud detection, there is still a lack of awareness around
fingerprinting. This work can hopefully form a basis for additional
exploration of this hidden side of the web.
