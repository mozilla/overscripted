## Overview

This is an implementation of the heuristics defined in _The Web's Sixth Sense: A Study of Scripts Accessing Smartphone Sensors_ 
by Anupam Das, Gunes Acar, Nikita Borisov and Amogh Pradeep. The heuristics are then run against the OverScripted dataset
to determine the prevalence of fingerprinting scripts and locations that call those scripts.

## Original Code

The open-source implementation of _The Web's Sixth Sense: A Study of Scripts Accessing Smartphone Sensors_ can be found on 
[GitHub](https://github.com/sensor-js/OpenWPM-mobile). All heuristics are implemented in 
[extract_features.py](https://github.com/sensor-js/OpenWPM-mobile/blob/mobile_sensors/feature_extraction/extract_features.py).

## Overall Stats

- Audio Fingerprinting: 170 scripts present on 2006 locations
- Canvas Fingerprinting: 8,514 scripts present on 38,419 locations
- CanvasFont Fingerprinting: 1,387 scripts present on 2,293 locations
- WebRTC Fingerprinting: 1,313 scripts present on 15,360 locations
