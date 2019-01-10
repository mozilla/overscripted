# Tracking Method Sources

## Web Tracking: Mechanisms, Implications, and Defenses
Note: This source covers almost all forms of fingerprinting detected or theorised
#### Session Only
* Session identifiers passed through links/requests
* Explicit web-form authentication
* window.name DOM property

#### Storage-based
* HTTP cookies
* Flash cookies and Java JNLP PersistenceService
* Flash LocalConnection object
* Silverlight Isolated Storage
* HTML5 Global, Local, and Session Storage
* Web SQL Database and HTML5 IndexedDB
* Internet Explorer userData storage

#### Cache-based
* Web cache
* Embedding identifiers in cached documents
* Loading performance tests
* ETags and Last-Modified headers
* DNS lookups
* Operational caches
* HTTP301 redirect cache
* HTTP authentication cache
* HTTP Strict Transport Security cache
* TLS Session Resumption cache and TLS Session IDs

#### Fingerprinting
* Network and location fingerprinting
* Device fingerprinting
* OS instance fingerprinting
* Browser version fingerprinting
* Browser instance fingerprinting using canvas
* Browser instance fingerprinting using web browsing history

#### Other Tracking mechanisms
* Headers attached to outgoing HTTP requests
* Using telephone metadata
* Timing attacks
* Using unconscious collaboration of the user
* Clickjacking
* Evercookies


## Hiding in the Crowd: an Analysis of the Effectiveness of Browser Fingerprinting at Large Scale  
Note: Color depth, encoding, do not track, and plugins are valuable additions to the list
* User-Agent
* Header-accept
* Content encoding
* Content language
* List of plugins
* Cookies enabled
* Use of local/session storage
* Timezone
* Screen resolution & color depth
* Available fonts
* List of HTTP headers
* Platform
* Do Not Track
* Canvas
* WebGL Vendor
* WebGL Renderer
* Use of an ad blocker

## The Web Never Forgets
* Canvas Fingerprinting
* Evercookies/Respawning
* Cookie Syncing
* Flash Cookies and using flash for respawning

## Fingerprinting Information in JavaScript Implementations
* Performance Fingerprinting
* Whitelist Fingerprinting

## Web Tracking – A Literature Review on the State of Research
TODO: Parse this list of papers for additional fingerprinting methods  
Stateful tracking:
* The Web Never Forgets: Persistant Tracking Mechanisms in the Wild - Acar et al. (2013, 2014)
* Hybrid Information Flow Monitoring Against Web Tracking - Besson et al. (2014)
* Web Tracking: Mechanisms, Implications, and Defenses - Bujlow et al. (2015, 2017)
* Online Tracking: A 1-million-site Measurement and Analysis - Englehardt & Narayanan (2016)
* Towards Seamless Tracking-Free Web: Improved Detection of Trackers via One-class Learning - Ikram et al. (2016)
* Third-Party Web Tracking: Policy and Technology - Mayer & Mitchell (2012)
* Web Tracking: Overview and applicability in digital investigations - Pugliese (2015)
* The Web is Watching You: A Comprehensive Review of Web-Tracking Techniques and Countermeasures - Sanchez-Rola et al. (2016) 

## Web tracking: Overview and applicability in digital investigation
Note: In “The Web Never Forgets” there is reference to this paper that mentions behavioural fingerprinting. I could not access the paper.  
“Pugliese (2015) also mentions behavioral biometric features, namely those dynamics that occur when typing, moving and clicking the mouse, or touching a touch screen. Such behavioral biometric features can be used to improve stateless tracking”

## Evaluating the effectiveness of defences to web tracking
https://www.royalholloway.ac.uk/media/5620/rhul-isg-2018-7-techreport-darrellnewman.pdf
Note: Lots to dig into here, not enough time this week to get through all of it
* Javascript Engines
* DOM Objects
* Installed add-ons/extensions
* Fonts
* Canvas API
* AudioContext API
* Battery Status API
* Emojis
* SSL/TLS Handshake Fingerprinting
* WebRTC fingerprinting
* Behavioural Biometrics

## Remote physical device fingerprinting
Note: This paper is from 2005
* Clock Skews

## Papers I couldn't access
SHPF: Enhancing HTTP(S) Session Security with Browser Fingerprinting  