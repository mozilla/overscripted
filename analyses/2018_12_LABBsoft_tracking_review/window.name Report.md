# window.name DOM property
### Summary
The window.name property stores up to 2MB of information that persists for the lifespan of a tab. This allows sites that are closed and revisited to reaccess whatever information they may have stored inside.

### Detection
#### In Literature
There were no examples of the detection of window.name trarcking found in the web tracking papers.

#### In The Overscripted Dataset
We found 2,484,730 instances of window.name access.

#### What else would we need to detect it?
We're equipped to track the calls to the window.name property. Detection could be improved if we logged the line of the window.name call.

#### Do we see it?
Using our symbol_counts.csv, we can check for all instances of the "window.navigator" interface and counting all instances.
```
count = 0
target = ["window.name"]
for line in f.split('\n'):
    for t in target:
        if t in line:
                count += int(line.split(",")[1])
                print(line)
```

Output:
```
window.name,2484730
```