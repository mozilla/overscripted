
This notebook processes the 2million+ json files into a cleaned data set.

It uses the following steps:

1. For every file in the ucosp bucket, downloads the json file from s3 and then:
  1. It corrects the raw_data so it can be parsed as rows of json
  1. Each row of json is validated against the defined JSON Schema 
  1. For bad rows, the reason for the failure is saved along with the data, the file number, and the row number
  1. For good rows, further processing is done
1. For good data, columns are processed to give clean dtypes such as int, bool, timestamp
1. Derived columns are computed e.g. the length of the value field
1. The bad and cleaned datasets are saved as parquet on s3 for future retrieval

### Imports and constants


```python
from __future__ import unicode_literals
from __future__ import division

import json
import pandas as pd

from ast import literal_eval
from jinja2 import Template
from jsonschema import Draft4Validator
from pyspark.sql.functions import length
from pyspark.sql.types import TimestampType
```


```python
BUCKET_NAME = 'Location of bucket where all json blobs are'
```

### Setup the schema

The schema holds a list of enums for symbol, that are stored in a csv, so we put in at runtime using jinja.

The schema is similar to validate_data_util.py but has some differences:


Things that validate_data_util does, that this validation does not do:

1. This validation does not do all the validation of call_stack checking per line entries. Reason: I could not capture that in a regex pattern
1. This validation allows anything for function name. Reason: There are many invalid values for a function name that are present in the dataset, not just not having a number at the front. So only excluding those with a number at start seemed inconsistent.


Additional things that this validation does:

1. It includes an additional enum for operation `set (failed)`
1. It includes enums for symbol
1. It adds some alternative regexes for timestamps as some were being thrown out unecessarily


```python
# Prepare schema
symbol_counts = pd.read_csv('symbol_counts.csv', names=['symbol', 'count'])
with open('raw_data_schema.template', 'r') as f:
    schema_template = Template(f.read())
schema = literal_eval(
    schema_template.render(
        list_of_symbols=list(symbol_counts.symbol.values)
    )
)
```

Pretty print it for reference.

You can copy-paste this to a JSON viewer like: http://jsonviewer.stack.hu/ to see it more structured.


```python
print(json.dumps(schema, indent=4, sort_keys=True))
```

    {
        "$schema": "http://json-schema.org/draft-04/schema#", 
        "description": "The schema for a row of the raw data in the crawl catalog. (The final dataset as additional derived columns)", 
        "properties": {
            "arguments": {
                "description": "Any arguments passed to the javascript call. When present takes the form of an object with numeric string keys e.g. '0', '1', up to a max of '9'. Validator does not check for this yet as couldn't find a satisfactory regex", 
                "type": "string"
            }, 
            "call_stack": {
                "description": "69% of calls have no call_stack. Where there is a call_stack, it appears you can: split on '\n' and get the same values that are in func_name, script_url, script_col, script_line - func_name@script_url:script_line:script_col", 
                "pattern": "^$|^(?!undefined).*$|", 
                "type": "string"
            }, 
            "crawl_id": {
                "const": 1, 
                "description": "The ID for this crawl"
            }, 
            "func_name": {
                "description": "Empty string or the name of the function that was executed. Note more liberal than current validation.", 
                "type": "string"
            }, 
            "in_iframe": {
                "description": "Was JS being exectuted in an iframe.", 
                "type": "boolean"
            }, 
            "location": {
                "description": "The location of the loaded page where from which javascript calls are being captured.", 
                "format": "uri", 
                "pattern": "^(https?|http?):\\/\\/\\S*", 
                "type": "string"
            }, 
            "operation": {
                "description": "The type of operation.", 
                "enum": [
                    "get", 
                    "set", 
                    "call", 
                    "set (failed)"
                ], 
                "type": "string"
            }, 
            "script_col": {
                "description": "The column location in the script where the call is captured. We want this to be an integer, but we must test for numeric string.", 
                "pattern": "^$|^[0-9]+$", 
                "type": "string"
            }, 
            "script_line": {
                "description": "The line location in the script where the call is captured. We want this to be an integer, but we must test for numeric string.", 
                "pattern": "^[0-9]+$", 
                "type": "string"
            }, 
            "script_loc_eval": {
                "description": "Empty string or .... What is this?", 
                "pattern": "^$|^(line [0-9]* > (eval|Function)[ ]?)*$", 
                "type": "string"
            }, 
            "script_url": {
                "description": "The location of the script url that is being executed. Liberally letting things through to see what's there.", 
                "minLength": 1, 
                "type": "string"
            }, 
            "symbol": {
                "description": "The js Symbol. Has 282 possible values in this dataset (this is derived there are more possible symbols in JS)", 
                "enum": [
                    "window.document.cookie", 
                    "window.navigator.userAgent", 
                    "window.Storage.getItem", 
                    "window.localStorage", 
                    "window.Storage.setItem", 
                    "window.sessionStorage", 
                    "window.Storage.removeItem", 
                    "window.name", 
                    "CanvasRenderingContext2D.fillStyle", 
                    "window.navigator.plugins[Shockwave Flash].description", 
                    "window.screen.colorDepth", 
                    "window.navigator.appName", 
                    "window.navigator.language", 
                    "window.navigator.platform", 
                    "CanvasRenderingContext2D.save", 
                    "CanvasRenderingContext2D.restore", 
                    "CanvasRenderingContext2D.fill", 
                    "CanvasRenderingContext2D.fillRect", 
                    "window.navigator.plugins[Shockwave Flash].name", 
                    "CanvasRenderingContext2D.font", 
                    "CanvasRenderingContext2D.lineWidth", 
                    "window.navigator.appVersion", 
                    "window.navigator.cookieEnabled", 
                    "HTMLCanvasElement.width", 
                    "CanvasRenderingContext2D.strokeStyle", 
                    "HTMLCanvasElement.height", 
                    "HTMLCanvasElement.getContext", 
                    "window.Storage.key", 
                    "CanvasRenderingContext2D.fillText", 
                    "window.Storage.length", 
                    "CanvasRenderingContext2D.stroke", 
                    "CanvasRenderingContext2D.measureText", 
                    "window.navigator.vendor", 
                    "window.navigator.doNotTrack", 
                    "CanvasRenderingContext2D.arc", 
                    "HTMLCanvasElement.style", 
                    "CanvasRenderingContext2D.textBaseline", 
                    "window.navigator.product", 
                    "CanvasRenderingContext2D.textAlign", 
                    "window.navigator.plugins[Shockwave Flash].filename", 
                    "window.navigator.mimeTypes[application/x-shockwave-flash].type", 
                    "window.navigator.languages", 
                    "window.navigator.plugins[Shockwave Flash].length", 
                    "CanvasRenderingContext2D.bezierCurveTo", 
                    "CanvasRenderingContext2D.shadowBlur", 
                    "CanvasRenderingContext2D.shadowOffsetY", 
                    "CanvasRenderingContext2D.shadowOffsetX", 
                    "CanvasRenderingContext2D.shadowColor", 
                    "window.screen.pixelDepth", 
                    "CanvasRenderingContext2D.rect", 
                    "HTMLCanvasElement.nodeType", 
                    "CanvasRenderingContext2D.lineJoin", 
                    "window.navigator.mimeTypes[application/futuresplash].type", 
                    "CanvasRenderingContext2D.lineCap", 
                    "window.navigator.plugins[Shockwave Flash].version", 
                    "CanvasRenderingContext2D.strokeRect", 
                    "HTMLCanvasElement.toDataURL", 
                    "CanvasRenderingContext2D.createRadialGradient", 
                    "CanvasRenderingContext2D.globalCompositeOperation", 
                    "window.navigator.onLine", 
                    "CanvasRenderingContext2D.scale", 
                    "window.Storage.hasOwnProperty", 
                    "CanvasRenderingContext2D.clip", 
                    "CanvasRenderingContext2D.miterLimit", 
                    "window.navigator.mimeTypes[application/x-shockwave-flash].suffixes", 
                    "window.navigator.mimeTypes[application/futuresplash].suffixes", 
                    "RTCPeerConnection.localDescription", 
                    "window.navigator.productSub", 
                    "window.navigator.mimeTypes[application/x-shockwave-flash].description", 
                    "window.navigator.mimeTypes[application/futuresplash].description", 
                    "HTMLCanvasElement.nodeName", 
                    "CanvasRenderingContext2D.rotate", 
                    "HTMLCanvasElement.parentNode", 
                    "window.navigator.oscpu", 
                    "window.navigator.appCodeName", 
                    "CanvasRenderingContext2D.createLinearGradient", 
                    "CanvasRenderingContext2D.putImageData", 
                    "window.navigator.geolocation", 
                    "CanvasRenderingContext2D.getImageData", 
                    "HTMLCanvasElement.ownerDocument", 
                    "HTMLCanvasElement.className", 
                    "RTCPeerConnection.onicecandidate", 
                    "HTMLCanvasElement.getAttribute", 
                    "window.navigator.vendorSub", 
                    "HTMLCanvasElement.addEventListener", 
                    "window.navigator.buildID", 
                    "HTMLCanvasElement.classList", 
                    "HTMLCanvasElement.setAttribute", 
                    "HTMLCanvasElement.clientHeight", 
                    "HTMLCanvasElement.clientWidth", 
                    "HTMLCanvasElement.getElementsByTagName", 
                    "HTMLCanvasElement.tagName", 
                    "RTCPeerConnection.iceGatheringState", 
                    "RTCPeerConnection.createDataChannel", 
                    "RTCPeerConnection.signalingState", 
                    "RTCPeerConnection.remoteDescription", 
                    "RTCPeerConnection.createOffer", 
                    "CanvasRenderingContext2D.setLineDash", 
                    "HTMLCanvasElement.onselectstart", 
                    "RTCPeerConnection.setLocalDescription", 
                    "CanvasRenderingContext2D.arcTo", 
                    "CanvasRenderingContext2D.isPointInPath", 
                    "CanvasRenderingContext2D.createImageData", 
                    "HTMLCanvasElement.id", 
                    "CanvasRenderingContext2D.imageSmoothingEnabled", 
                    "HTMLCanvasElement.draggable", 
                    "HTMLCanvasElement.constructor", 
                    "CanvasRenderingContext2D.createPattern", 
                    "CanvasRenderingContext2D.lineDashOffset", 
                    "HTMLCanvasElement.offsetWidth", 
                    "CanvasRenderingContext2D.mozImageSmoothingEnabled", 
                    "RTCPeerConnection.idpLoginUrl", 
                    "RTCPeerConnection.peerIdentity", 
                    "RTCPeerConnection.onremovestream", 
                    "HTMLCanvasElement.offsetHeight", 
                    "CanvasRenderingContext2D.strokeText", 
                    "HTMLCanvasElement.firstChild", 
                    "HTMLCanvasElement.hasAttribute", 
                    "HTMLCanvasElement.localName", 
                    "HTMLCanvasElement.attributes", 
                    "HTMLCanvasElement.nextSibling", 
                    "AudioContext.destination", 
                    "HTMLCanvasElement.firstElementChild", 
                    "HTMLCanvasElement.nextElementSibling", 
                    "window.Storage.clear", 
                    "HTMLCanvasElement.dir", 
                    "CanvasRenderingContext2D.mozCurrentTransform", 
                    "OscillatorNode.frequency", 
                    "AudioContext.createOscillator", 
                    "OscillatorNode.start", 
                    "CanvasRenderingContext2D.__lookupGetter__", 
                    "HTMLCanvasElement.childNodes", 
                    "CanvasRenderingContext2D.hasOwnProperty", 
                    "HTMLCanvasElement.getBoundingClientRect", 
                    "HTMLCanvasElement.offsetLeft", 
                    "OscillatorNode.type", 
                    "OscillatorNode.connect", 
                    "CanvasRenderingContext2D.mozCurrentTransformInverse", 
                    "HTMLCanvasElement.removeAttribute", 
                    "HTMLCanvasElement.offsetTop", 
                    "HTMLCanvasElement.children", 
                    "HTMLCanvasElement.dispatchEvent", 
                    "HTMLCanvasElement.mozOpaque", 
                    "HTMLCanvasElement.onmousemove", 
                    "AudioContext.createDynamicsCompressor", 
                    "HTMLCanvasElement.offsetParent", 
                    "OfflineAudioContext.startRendering", 
                    "OfflineAudioContext.createDynamicsCompressor", 
                    "OfflineAudioContext.oncomplete", 
                    "OfflineAudioContext.createOscillator", 
                    "OfflineAudioContext.destination", 
                    "HTMLCanvasElement.remove", 
                    "HTMLCanvasElement.compareDocumentPosition", 
                    "AudioContext.state", 
                    "AudioContext.listener", 
                    "GainNode.connect", 
                    "AudioContext.createGain", 
                    "GainNode.gain", 
                    "HTMLCanvasElement.__proto__", 
                    "window.Storage.toString", 
                    "AudioContext.createAnalyser", 
                    "HTMLCanvasElement.cloneNode", 
                    "AudioContext.sampleRate", 
                    "AudioContext.decodeAudioData", 
                    "AudioContext.createMediaElementSource", 
                    "HTMLCanvasElement.toBlob", 
                    "HTMLCanvasElement.removeEventListener", 
                    "AnalyserNode.fftSize", 
                    "AnalyserNode.maxDecibels", 
                    "AnalyserNode.smoothingTimeConstant", 
                    "AnalyserNode.frequencyBinCount", 
                    "AnalyserNode.minDecibels", 
                    "RTCPeerConnection.addIceCandidate", 
                    "AudioContext.onstatechange", 
                    "HTMLCanvasElement.textContent", 
                    "HTMLCanvasElement.onclick", 
                    "HTMLCanvasElement.innerHTML", 
                    "window.Storage.valueOf", 
                    "RTCPeerConnection.setRemoteDescription", 
                    "RTCPeerConnection.getStats", 
                    "AudioContext.currentTime", 
                    "OscillatorNode.stop", 
                    "RTCPeerConnection.removeEventListener", 
                    "RTCPeerConnection.addEventListener", 
                    "HTMLCanvasElement.__lookupGetter__", 
                    "AudioContext.createScriptProcessor", 
                    "HTMLCanvasElement.hasOwnProperty", 
                    "HTMLCanvasElement.onmousedown", 
                    "HTMLCanvasElement.toString", 
                    "ScriptProcessorNode.connect", 
                    "ScriptProcessorNode.onaudioprocess", 
                    "AnalyserNode.connect", 
                    "HTMLCanvasElement.blur", 
                    "HTMLCanvasElement.getAttributeNode", 
                    "HTMLCanvasElement.onmouseout", 
                    "HTMLCanvasElement.onmouseover", 
                    "HTMLCanvasElement.append", 
                    "HTMLCanvasElement.onmouseup", 
                    "CanvasRenderingContext2D.ellipse", 
                    "HTMLCanvasElement.setAttributeNode", 
                    "HTMLCanvasElement.oncontextmenu", 
                    "CanvasRenderingContext2D.getLineDash", 
                    "HTMLCanvasElement.previousSibling", 
                    "HTMLCanvasElement.parentElement", 
                    "HTMLCanvasElement.innerText", 
                    "HTMLCanvasElement.onkeydown", 
                    "HTMLCanvasElement.onkeyup", 
                    "HTMLCanvasElement.onkeypress", 
                    "HTMLCanvasElement.onblur", 
                    "HTMLCanvasElement.onfocus", 
                    "HTMLCanvasElement.onmouseleave", 
                    "HTMLCanvasElement.ondblclick", 
                    "HTMLCanvasElement.ondragenter", 
                    "HTMLCanvasElement.onresize", 
                    "HTMLCanvasElement.onpaste", 
                    "HTMLCanvasElement.onchange", 
                    "HTMLCanvasElement.oncut", 
                    "HTMLCanvasElement.ondragover", 
                    "HTMLCanvasElement.ondragleave", 
                    "HTMLCanvasElement.ondrop", 
                    "HTMLCanvasElement.onmouseenter", 
                    "HTMLCanvasElement.onload", 
                    "HTMLCanvasElement.contains", 
                    "HTMLCanvasElement.querySelectorAll", 
                    "GainNode.disconnect", 
                    "AudioContext.createBufferSource", 
                    "HTMLCanvasElement.hasChildNodes", 
                    "AudioContext.createBuffer", 
                    "AudioContext.createPanner", 
                    "HTMLCanvasElement.scrollLeft", 
                    "HTMLCanvasElement.scrollTop", 
                    "CanvasRenderingContext2D.__lookupSetter__", 
                    "CanvasRenderingContext2D.__defineSetter__", 
                    "HTMLCanvasElement.ondragstart", 
                    "HTMLCanvasElement.getClientRects", 
                    "HTMLCanvasElement.title", 
                    "HTMLCanvasElement.tabIndex", 
                    "RTCPeerConnection.close", 
                    "RTCPeerConnection.iceConnectionState", 
                    "AudioContext.close", 
                    "HTMLCanvasElement.hasAttributes", 
                    "HTMLCanvasElement.previousElementSibling", 
                    "OscillatorNode.disconnect", 
                    "HTMLCanvasElement.focus", 
                    "RTCPeerConnection.onsignalingstatechange", 
                    "RTCPeerConnection.oniceconnectionstatechange", 
                    "HTMLCanvasElement.valueOf", 
                    "HTMLCanvasElement.dataset", 
                    "HTMLCanvasElement.requestPointerLock", 
                    "HTMLCanvasElement.namespaceURI", 
                    "HTMLCanvasElement.webkitMatchesSelector", 
                    "HTMLCanvasElement.childElementCount", 
                    "HTMLCanvasElement.removeChild", 
                    "HTMLCanvasElement.insertBefore", 
                    "GainNode.numberOfOutputs", 
                    "HTMLCanvasElement.matches", 
                    "HTMLCanvasElement.outerHTML", 
                    "HTMLCanvasElement.appendChild", 
                    "AudioContext.resume", 
                    "AnalyserNode.getByteFrequencyData", 
                    "HTMLCanvasElement.clientTop", 
                    "HTMLCanvasElement.clientLeft", 
                    "HTMLCanvasElement.onwheel", 
                    "HTMLCanvasElement.DOCUMENT_NODE", 
                    "RTCPeerConnection.onaddstream", 
                    "AnalyserNode.channelInterpretation", 
                    "AnalyserNode.numberOfInputs", 
                    "AnalyserNode.channelCountMode", 
                    "AnalyserNode.numberOfOutputs", 
                    "AnalyserNode.channelCount", 
                    "HTMLCanvasElement.scrollWidth", 
                    "HTMLCanvasElement.scrollHeight", 
                    "CanvasRenderingContext2D.__proto__", 
                    "HTMLCanvasElement.getElementsByClassName", 
                    "CanvasRenderingContext2D.__defineGetter__", 
                    "HTMLCanvasElement.querySelector", 
                    "OfflineAudioContext.decodeAudioData", 
                    "RTCPeerConnection.createAnswer", 
                    "CanvasRenderingContext2D.filter", 
                    "AudioContext.createConvolver", 
                    "HTMLCanvasElement.lastChild", 
                    "CanvasRenderingContext2D.toString"
                ], 
                "type": "string"
            }, 
            "time_stamp": {
                "description": "Time at which call was captured. Valid timestamps 2017-12-16T10:12:58Z, 2017-12-16T10:12:58.000Z, 2017-12-16T10:12:58+0000 ", 
                "format": "date-time", 
                "pattern": "^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}.?\\d{0,3}Z$|^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}\\+\\d{4}$", 
                "type": "string"
            }, 
            "value": {
                "description": "The value that was passed to the javascript call. Can be a few or over 1million characters.", 
                "type": "string"
            }
        }, 
        "required": [
            "call_stack", 
            "crawl_id", 
            "func_name", 
            "in_iframe", 
            "location", 
            "operation", 
            "script_col", 
            "script_line", 
            "script_loc_eval", 
            "script_url", 
            "symbol", 
            "time_stamp", 
            "value"
        ], 
        "title": "UCOSP Crawl - Call Schema", 
        "type": "object"
    }



```python
# Broadcast the schema to all the workers
schema = sc.broadcast(schema)
```

### Process the data


```python
COLUMNS = (
    'argument_0',
    'argument_1',
    'argument_2',
    'argument_3',
    'argument_4',
    'argument_5',
    'argument_6',
    'argument_7',
    'argument_8',
    'arguments',
    'arguments_n_keys',
    'call_id',
    'call_stack',
    'crawl_id',
    'file_name',
    'func_name',
    'in_iframe',
    'location',
    'operation',
    'script_col',
    'script_line',
    'script_loc_eval',
    'script_url',
    'symbol',
    'time_stamp',
    'value',
    'value_1000',
    'value_len',
    # Validator Columns
    'valid',
    'errors'
)
```


```python
def get_rows_from_raw_data(raw_data):
    # Setup dummy row incase something goes wrong
    rows = [{'errors': ''}]
    try:
        data = "[" + raw_data[1:-1] + "]"
        rows = json.loads(data)
    except ValueError as e:
        rows[0]['errors'] = 'Error converting raw_data into json: {}'.format(e.message)
    except:
        rows[0]['errors'] = 'Unknown error when reading data.'
    return rows


def get_json_schema_errors(row, validator):
    errors = ''
    for error in validator.iter_errors(row):
        try:
            bad_value_truncated = error.instance[:75] + (error.instance[75:] and '...')
            errors += '{}: {} not valid ||\n'.format(error.path[0], bad_value_truncated)
        except:
            errors += 'Could not parse JSON Schema error.'
    return errors


def convert_to_dict(item):
    item = item.replace('false', 'False')
    item = item.replace('true', 'True')
    item = item.replace('null', 'None')
    try:
        return literal_eval(item)
    except:
        return {}


def process_arguments(row):
    if 'arguments' not in row.keys():
        row['arguments'] = '{}'
    _arguments = convert_to_dict(row['arguments'])
    n_args = len(_arguments)
    row["arguments_n_keys"] = n_args
    for n in range(n_args):
        key = 'argument_{}'.format(n)
        row[key] = _arguments.get(str(n), "")
    return row


def validate_and_process_file(whole_text_file_row):    
    file_name = whole_text_file_row[0].split(BUCKET_NAME)[1]
    raw_data = whole_text_file_row[1]
    
    validator = Draft4Validator(schema.value)
    rows = get_rows_from_raw_data(raw_data)
    
    for i, row in enumerate(rows):
        errors = row.get('errors')

        if errors is None:
            valid = validator.is_valid(row)
            if valid is False:
                errors = get_json_schema_errors(row, validator)
            else:
                errors = ''
        else: 
            valid = False
        
        row['file_name'] = '{}'.format(file_name)
        row['call_id'] = '{}__{}'.format(file_name, i)
        row['valid'] = valid
        row['errors'] = errors
        
        if valid is True:
            row = process_arguments(row)
        
    return rows
```


```python
%%time
# These lines take a long time when there are lots of files 
# (30s for 100k files, ~30min for 2m+ files)

filesRDD = sc.wholeTextFiles(BUCKET_NAME, minPartitions=3000)

validated_rows = filesRDD.flatMap(validate_and_process_file)

validated_rows_mapped = validated_rows.map(lambda x : tuple(x.get(col, "") for col in COLUMNS))

validated_df = spark.createDataFrame(validated_rows_mapped, schema=COLUMNS)
```

    CPU times: user 248 ms, sys: 96 ms, total: 344 ms
    Wall time: 32min



```python
# Get the good rows
good_rows = validated_df[validated_df.valid == True]

# Add the value_len column
good_rows = good_rows.withColumn('value_len', length(good_rows.value))

# Add the column with the initial values from value
good_rows = good_rows.withColumn('value_1000', good_rows.value.substr(0, 1000))

# Set timestamp and remove bad values
good_rows = good_rows.withColumn('time_stamp', good_rows.time_stamp.cast(TimestampType()))

# Keep good_rows at just 3000 partitions
good_rows = good_rows.coalesce(3000)

# Let's look at the dtypes
good_rows.dtypes
```




    [('argument_0', 'string'),
     ('argument_1', 'string'),
     ('argument_2', 'string'),
     ('argument_3', 'string'),
     ('argument_4', 'string'),
     ('argument_5', 'string'),
     ('argument_6', 'string'),
     ('argument_7', 'string'),
     ('argument_8', 'string'),
     ('arguments', 'string'),
     ('arguments_n_keys', 'bigint'),
     ('call_id', 'string'),
     ('call_stack', 'string'),
     ('crawl_id', 'bigint'),
     ('file_name', 'string'),
     ('func_name', 'string'),
     ('in_iframe', 'boolean'),
     ('location', 'string'),
     ('operation', 'string'),
     ('script_col', 'string'),
     ('script_line', 'string'),
     ('script_loc_eval', 'string'),
     ('script_url', 'string'),
     ('symbol', 'string'),
     ('time_stamp', 'timestamp'),
     ('value', 'string'),
     ('value_1000', 'string'),
     ('value_len', 'int'),
     ('valid', 'boolean'),
     ('errors', 'string')]




```python
# Now setup bad_rows
bad_rows = validated_df[validated_df.valid == False]

# Shrink bad_rows to 100 (we expect it to be much smaller)
bad_rows = bad_rows.coalesce(100)
```

### Save data


```python
good_location = "{}clean.parquet".format(BUCKET_NAME)
bad_location = "{}invalid.parquet".format(BUCKET_NAME)
```


```python
%%time
good_rows.write.parquet(good_location)
```

    CPU times: user 1.22 s, sys: 556 ms, total: 1.78 s
    Wall time: 4h 22min 13s



```python
%%time
bad_rows.write.parquet(bad_location)
```

    CPU times: user 500 ms, sys: 212 ms, total: 712 ms
    Wall time: 2h 9min 23s

