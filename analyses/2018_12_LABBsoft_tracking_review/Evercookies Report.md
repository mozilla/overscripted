# Evercookies
### Summary
The practice of restoring cleared cookies by storing the cookie information in an alternate location and recreating the cookie if it has been removed. This preserves the lifespan of the cookies and allows sites to identify users that are clearing their cookies.

Should other cookie behaviour such as duplicating cookies to all browsers on a system or passing cookies between domains count as evercookies?

### Detection
#### In Literature
The TOR Browser design draft identifies the following locations for identifier storage:
- **Cookies**
- **Cache**
- **HTTP Authentication**
- **DOM Storage**
- IndexedDB Storage
- **Flash Cookies**
- SSL+TLS session resumption
- Javascript SharedWorkers - threads with a shared scope between all threads from the same JS origin, could have access to objects from the same third party loaded at another origin
- URL.createObjectURL
- SPDY, HTTP/2
- Cross-origin redirects
- **window.name**
- Auto form-fill
- HSTS - Stores an effective bit of information per domain name
- HPKP 
- BroadcastChannel API
- OCSP Requests
- Favicons
- mediasource URIs and MediaStreams
- Speculative and prefetched connections
- Permissions API



#### In The Overscripted Dataset
We found 52,669,910 instances of local storage access, cookie data access or window.name access.

#### What else would we need to detect it?
The best way to detect evercookies would be multiple runs of the same crawl while clearing cache between attempts. This would allow us to compare cookies between attempts as well as log the state of all possible storage mechanisms after each run.


#### Do we see it?
Using our symbol_counts.csv, we can check for all instances of the "window.navigator" interface and counting all instances.
```
count = 0
target = ["window.name", "setItem", "getItem", "document.cookie"]
for line in f.split('\n'):
    for t in target:
        if t in line:
                count += int(line.split(",")[1])
                print(line)
print("Total:", count)
```

Output:
```
window.document.cookie,35455680
window.Storage.getItem,10553944
window.Storage.setItem,4175556
window.name,2484730
Total: 52669910
```