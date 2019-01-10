# Browser Version Identification
### Summary
Identifying web browsing software and version is a core component of a stateless fingerprint. In most cases the user will provide a genuine User-Agent request header that will contain the browser type, version, developer and the operating system. Some browsers are obfuscating this header to protect the user's privacy. Unfortunately, because of small differences between browsers there exist ways to detect a forged User-Agent string.

### Detection
#### In Literature
The User-Agent string is available through the Navigator interface, so any usage of window.navigator will be accessing User-Agent data. 
However, a site owner could manually parse the request headers to access that data without using the Navigator interface.
Identifying forged User-Agents is browser version specific. In _How Unique Is Your Web Browser_ they found forged strings when they noticed there were iOS devices that had flash enabled.

#### In The Overscripted Dataset
The Navigator interface was detected 26,361,700 times in the overscripted dataset.
I don't know how to identify if a Navigator interface was called for tracking purposes or for functionality (to display an error message on IE6 for example)


#### What else would we need to detect it?
The dataset allows us to identify when a website accesses the User-Agent through the Navigator interface. 
It may be possible to identify sites that test for forged User-Agents by crawling with a specific User-Agent string and checking for calls to unsupported features.

#### Do we see it?
Using our symbol_counts.csv, we can check for all instances of the "window.navigator" interface and counting all instances.
```
count = 0
for line in f.split('\n'):
    if "window.navigator" in line:
        count += int(line.split(",")[1])
        print(line[17:])
print("Total:", count)
```

Output:
```
userAgent,15534371
plugins[Shockwave Flash].description,1863285
appName,1286084
language,1172256
platform,1140738
plugins[Shockwave Flash].name,895289
appVersion,707298
cookieEnabled,692524
vendor,487833
doNotTrack,468365
product,279653
plugins[Shockwave Flash].filename,225751
mimeTypes[application/x-shockwave-flash].type,213769
languages,199435
plugins[Shockwave Flash].length,184995
mimeTypes[application/futuresplash].type,150364
plugins[Shockwave Flash].version,144656
onLine,116037
mimeTypes[application/x-shockwave-flash].suffixes,94030
mimeTypes[application/futuresplash].suffixes,94025
productSub,71139
mimeTypes[application/x-shockwave-flash].description,70284
mimeTypes[application/futuresplash].description,70278
oscpu,54799
appCodeName,51161
geolocation,43022
vendorSub,26840
buildID,23419
Total: 26361700
```