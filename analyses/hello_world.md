
### Load and have a quick look at the data with pandas, dask and spark


* [Pandas](#Pandas)
* [Dask](#Dask)
* [Spark](#Spark)


```python
import tldextract

DATA_DIR = 'path to where you have extracted the data'
PARQUET_FILE = DATA_DIR + 'sample'  # I ran this with sample data*

def extract_domain(url):
    """Use tldextract to return the base domain from a url"""
    try:
        extracted = tldextract.extract(url)
        return '{}.{}'.format(extracted.domain, extracted.suffix)
    except Exception as e:
        return 'ERROR'
```

<small>*could also be run with full data (but beware of pandas blowing up RAM)</small>


# Pandas

http://pandas.pydata.org/


```python
import pandas as pd
```


```python
df = pd.read_parquet(PARQUET_FILE, engine='pyarrow')
df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>argument_0</th>
      <th>argument_1</th>
      <th>argument_2</th>
      <th>argument_3</th>
      <th>argument_4</th>
      <th>argument_5</th>
      <th>argument_6</th>
      <th>argument_7</th>
      <th>argument_8</th>
      <th>arguments</th>
      <th>...</th>
      <th>script_line</th>
      <th>script_loc_eval</th>
      <th>script_url</th>
      <th>symbol</th>
      <th>time_stamp</th>
      <th>value</th>
      <th>value_1000</th>
      <th>value_len</th>
      <th>valid</th>
      <th>errors</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>{}</td>
      <td>...</td>
      <td>57</td>
      <td></td>
      <td>https://staticxx.facebook.com/connect/xd_arbit...</td>
      <td>window.name</td>
      <td>2017-12-16 02:54:10.079</td>
      <td>fb_xdm_frame_https</td>
      <td>fb_xdm_frame_https</td>
      <td>18</td>
      <td>True</td>
      <td></td>
    </tr>
    <tr>
      <th>1</th>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>{}</td>
      <td>...</td>
      <td>57</td>
      <td></td>
      <td>https://staticxx.facebook.com/connect/xd_arbit...</td>
      <td>window.name</td>
      <td>2017-12-16 02:54:10.080</td>
      <td>fb_xdm_frame_https</td>
      <td>fb_xdm_frame_https</td>
      <td>18</td>
      <td>True</td>
      <td></td>
    </tr>
    <tr>
      <th>2</th>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>{}</td>
      <td>...</td>
      <td>57</td>
      <td></td>
      <td>https://staticxx.facebook.com/connect/xd_arbit...</td>
      <td>window.document.cookie</td>
      <td>2017-12-16 02:54:10.086</td>
      <td></td>
      <td></td>
      <td>0</td>
      <td>True</td>
      <td></td>
    </tr>
    <tr>
      <th>3</th>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>{}</td>
      <td>...</td>
      <td>49</td>
      <td></td>
      <td>https://staticxx.facebook.com/connect/xd_arbit...</td>
      <td>window.navigator.userAgent</td>
      <td>2017-12-16 02:54:10.088</td>
      <td>Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko...</td>
      <td>Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko...</td>
      <td>68</td>
      <td>True</td>
      <td></td>
    </tr>
    <tr>
      <th>4</th>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>{}</td>
      <td>...</td>
      <td>25</td>
      <td></td>
      <td>https://ajax.googleapis.com/ajax/libs/webfont/...</td>
      <td>window.navigator.userAgent</td>
      <td>2017-12-16 07:12:07.104</td>
      <td>Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko...</td>
      <td>Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko...</td>
      <td>68</td>
      <td>True</td>
      <td></td>
    </tr>
  </tbody>
</table>
<p>5 rows × 30 columns</p>
</div>




```python
df.columns
```




    Index(['argument_0', 'argument_1', 'argument_2', 'argument_3', 'argument_4',
           'argument_5', 'argument_6', 'argument_7', 'argument_8', 'arguments',
           'arguments_n_keys', 'call_id', 'call_stack', 'crawl_id', 'file_name',
           'func_name', 'in_iframe', 'location', 'operation', 'script_col',
           'script_line', 'script_loc_eval', 'script_url', 'symbol', 'time_stamp',
           'value', 'value_1000', 'value_len', 'valid', 'errors'],
          dtype='object')




```python
df['location_domain'] = df.location.apply(extract_domain)
df['script_domain'] = df.script_url.apply(extract_domain)
```


```python
df.location_domain.value_counts().head()
```




    gap.com               736
    officeworks.com.au    708
    ufc.ca                518
    doubleclick.net       517
    disqus.com            479
    Name: location_domain, dtype: int64




```python
df.script_domain.value_counts().head(10)
```




    google-analytics.com    1317
    optimizely.com           573
    yandex.ru                422
    baidu.com                416
    doubleclick.net          407
    cloudfront.net           385
    moatads.com              287
    disquscdn.com            273
    fbcdn.net                256
    gap.com                  233
    Name: script_domain, dtype: int64



How many domains have google analytics and yandex.ru?


```python
google_analytics = df[df.script_domain == 'google-analytics.com']
yandex = df[df.script_domain == 'yandex.ru']
```


```python
for location_domain in google_analytics.location_domain.unique():
    if location_domain in list(yandex.location_domain.unique()):
        print(location_domain)
```

    vjav.com
    newchic.com
    zona.mobi


# Dask

http://dask.pydata.org/


```python
import dask.dataframe as dd
from dask.diagnostics import ProgressBar
```


```python
ddf = dd.read_parquet(PARQUET_FILE, engine='pyarrow')
ddf.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>argument_0</th>
      <th>argument_1</th>
      <th>argument_2</th>
      <th>argument_3</th>
      <th>argument_4</th>
      <th>argument_5</th>
      <th>argument_6</th>
      <th>argument_7</th>
      <th>argument_8</th>
      <th>arguments</th>
      <th>...</th>
      <th>script_line</th>
      <th>script_loc_eval</th>
      <th>script_url</th>
      <th>symbol</th>
      <th>time_stamp</th>
      <th>value</th>
      <th>value_1000</th>
      <th>value_len</th>
      <th>valid</th>
      <th>errors</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>{}</td>
      <td>...</td>
      <td>57</td>
      <td></td>
      <td>https://staticxx.facebook.com/connect/xd_arbit...</td>
      <td>window.name</td>
      <td>2017-12-16 02:54:10.079</td>
      <td>fb_xdm_frame_https</td>
      <td>fb_xdm_frame_https</td>
      <td>18</td>
      <td>True</td>
      <td></td>
    </tr>
    <tr>
      <th>1</th>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>{}</td>
      <td>...</td>
      <td>57</td>
      <td></td>
      <td>https://staticxx.facebook.com/connect/xd_arbit...</td>
      <td>window.name</td>
      <td>2017-12-16 02:54:10.080</td>
      <td>fb_xdm_frame_https</td>
      <td>fb_xdm_frame_https</td>
      <td>18</td>
      <td>True</td>
      <td></td>
    </tr>
    <tr>
      <th>2</th>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>{}</td>
      <td>...</td>
      <td>57</td>
      <td></td>
      <td>https://staticxx.facebook.com/connect/xd_arbit...</td>
      <td>window.document.cookie</td>
      <td>2017-12-16 02:54:10.086</td>
      <td></td>
      <td></td>
      <td>0</td>
      <td>True</td>
      <td></td>
    </tr>
    <tr>
      <th>3</th>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>{}</td>
      <td>...</td>
      <td>49</td>
      <td></td>
      <td>https://staticxx.facebook.com/connect/xd_arbit...</td>
      <td>window.navigator.userAgent</td>
      <td>2017-12-16 02:54:10.088</td>
      <td>Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko...</td>
      <td>Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko...</td>
      <td>68</td>
      <td>True</td>
      <td></td>
    </tr>
    <tr>
      <th>4</th>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>{}</td>
      <td>...</td>
      <td>25</td>
      <td></td>
      <td>https://ajax.googleapis.com/ajax/libs/webfont/...</td>
      <td>window.navigator.userAgent</td>
      <td>2017-12-16 07:12:07.104</td>
      <td>Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko...</td>
      <td>Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko...</td>
      <td>68</td>
      <td>True</td>
      <td></td>
    </tr>
  </tbody>
</table>
<p>5 rows × 30 columns</p>
</div>




```python
ddf.columns
```




    Index(['argument_0', 'argument_1', 'argument_2', 'argument_3', 'argument_4',
           'argument_5', 'argument_6', 'argument_7', 'argument_8', 'arguments',
           'arguments_n_keys', 'call_id', 'call_stack', 'crawl_id', 'file_name',
           'func_name', 'in_iframe', 'location', 'operation', 'script_col',
           'script_line', 'script_loc_eval', 'script_url', 'symbol', 'time_stamp',
           'value', 'value_1000', 'value_len', 'valid', 'errors'],
          dtype='object')



What are people putting in the canvas


```python
ddf['location_domain'] = ddf.location.apply(extract_domain, meta=('x', 'str'))
ddf['script_domain'] = ddf.script_url.apply(extract_domain, meta=('x', 'str'))
```


```python
fillTexts = ddf[ddf.symbol == 'CanvasRenderingContext2D.fillText']

with ProgressBar():
    fillTexts = fillTexts.compute()
```

    [########################################] | 100% Completed |  0.4s



```python
# What's being written to canvas
pd.DataFrame(fillTexts.argument_0.value_counts())
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>argument_0</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>ð</th>
      <td>8</td>
    </tr>
    <tr>
      <th>ð§ââï¸</th>
      <td>2</td>
    </tr>
    <tr>
      <th>ð§ââï¸</th>
      <td>2</td>
    </tr>
    <tr>
      <th>45</th>
      <td>2</td>
    </tr>
    <tr>
      <th>38</th>
      <td>2</td>
    </tr>
    <tr>
      <th>ðºð³</th>
      <td>2</td>
    </tr>
    <tr>
      <th>ClientJS,org &lt;canvas&gt; 1.0</th>
      <td>2</td>
    </tr>
    <tr>
      <th>ðºâð³</th>
      <td>2</td>
    </tr>
    <tr>
      <th>!H71JCaj)]# 1@#</th>
      <td>1</td>
    </tr>
    <tr>
      <th>Soft Ruddy Foothold 2</th>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>




```python
# How does it vary by domain?
pd.DataFrame(fillTexts.groupby(['location_domain', 'script_domain', 'argument_0']).size())
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th></th>
      <th>0</th>
    </tr>
    <tr>
      <th>location_domain</th>
      <th>script_domain</th>
      <th>argument_0</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="4" valign="top">bongacams.com</th>
      <th rowspan="4" valign="top">bongacams.com</th>
      <th>ðºâð³</th>
      <td>1</td>
    </tr>
    <tr>
      <th>ðºð³</th>
      <td>1</td>
    </tr>
    <tr>
      <th>ð§ââï¸</th>
      <td>1</td>
    </tr>
    <tr>
      <th>ð§ââï¸</th>
      <td>1</td>
    </tr>
    <tr>
      <th rowspan="3" valign="top">facebook.com</th>
      <th rowspan="3" valign="top">fbcdn.net</th>
      <th>38</th>
      <td>2</td>
    </tr>
    <tr>
      <th>45</th>
      <td>2</td>
    </tr>
    <tr>
      <th>ð</th>
      <td>8</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">gap.com</th>
      <th rowspan="2" valign="top">gap.com</th>
      <th>!H71JCaj)]# 1@#</th>
      <td>1</td>
    </tr>
    <tr>
      <th>Soft Ruddy Foothold 2</th>
      <td>1</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">syracuse.edu</th>
      <th rowspan="4" valign="top">syracuse.edu</th>
      <th>ðºâð³</th>
      <td>1</td>
    </tr>
    <tr>
      <th>ðºð³</th>
      <td>1</td>
    </tr>
    <tr>
      <th>ð§ââï¸</th>
      <td>1</td>
    </tr>
    <tr>
      <th>ð§ââï¸</th>
      <td>1</td>
    </tr>
    <tr>
      <th>urcosme.com</th>
      <th>amazonaws.com</th>
      <th>ClientJS,org &lt;canvas&gt; 1.0</th>
      <td>2</td>
    </tr>
  </tbody>
</table>
</div>



# Spark

https://spark.apache.org/docs/latest/api/python/pyspark.html

We use [findspark](https://github.com/minrk/findspark) to set up spark.


```python
import findspark

findspark.init('/opt/spark')  # Adjust for the location where you installed spark

from pyspark import SparkContext
from pyspark.sql import SparkSession

sc = SparkContext(appName="Overscripted")
spark = SparkSession(sc)
```

### Read in parquet and display a row


```python
sdf = spark.read.parquet(DATA_DIR + 'sample')
sdf.show(1, vertical=True, truncate=False)
```

    -RECORD 0-----------------------------------------------------------------------------------------------------------------------------------------------------
     argument_0       |                                                                                                                                           
     argument_1       |                                                                                                                                           
     argument_2       |                                                                                                                                           
     argument_3       |                                                                                                                                           
     argument_4       |                                                                                                                                           
     argument_5       |                                                                                                                                           
     argument_6       |                                                                                                                                           
     argument_7       |                                                                                                                                           
     argument_8       |                                                                                                                                           
     arguments        | {}                                                                                                                                        
     arguments_n_keys | 0                                                                                                                                         
     call_id          | 1_028048bbce3f7816a5f1277ac3ac2372d6607581a77a4bfb7a1873ab.json__0                                                                        
     call_stack       |                                                                                                                                           
     crawl_id         | 1                                                                                                                                         
     file_name        | 1_028048bbce3f7816a5f1277ac3ac2372d6607581a77a4bfb7a1873ab.json                                                                           
     func_name        | a/<                                                                                                                                       
     in_iframe        | true                                                                                                                                      
     location         | https://staticxx.facebook.com/connect/xd_arbiter/r/lY4eZXm_YWu.js?version=42#channel=f30ef17b61f384&origin=http%3A%2F%2Fwww.ubitennis.com 
     operation        | get                                                                                                                                       
     script_col       | 1802                                                                                                                                      
     script_line      | 57                                                                                                                                        
     script_loc_eval  |                                                                                                                                           
     script_url       | https://staticxx.facebook.com/connect/xd_arbiter/r/lY4eZXm_YWu.js?version=42#channel=f30ef17b61f384&origin=http%3A%2F%2Fwww.ubitennis.com 
     symbol           | window.name                                                                                                                               
     time_stamp       | 2017-12-16 04:54:10.079                                                                                                                   
     value            | fb_xdm_frame_https                                                                                                                        
     value_1000       | fb_xdm_frame_https                                                                                                                        
     value_len        | 18                                                                                                                                        
     valid            | true                                                                                                                                      
     errors           |                                                                                                                                           
    only showing top 1 row
    


### Get the distinct symbols and show highest counts


```python
sdf.select('symbol').distinct().show(truncate=False)
```

    +-------------------------------------------------------------+
    |symbol                                                       |
    +-------------------------------------------------------------+
    |window.navigator.appVersion                                  |
    |window.navigator.product                                     |
    |window.screen.colorDepth                                     |
    |RTCPeerConnection.createOffer                                |
    |RTCPeerConnection.localDescription                           |
    |CanvasRenderingContext2D.font                                |
    |HTMLCanvasElement.nodeType                                   |
    |CanvasRenderingContext2D.createRadialGradient                |
    |RTCPeerConnection.onicecandidate                             |
    |window.navigator.buildID                                     |
    |CanvasRenderingContext2D.scale                               |
    |window.navigator.mimeTypes[application/futuresplash].suffixes|
    |RTCPeerConnection.setLocalDescription                        |
    |CanvasRenderingContext2D.fillText                            |
    |CanvasRenderingContext2D.fill                                |
    |window.navigator.appName                                     |
    |HTMLCanvasElement.style                                      |
    |HTMLCanvasElement.className                                  |
    |HTMLCanvasElement.getContext                                 |
    |window.navigator.doNotTrack                                  |
    +-------------------------------------------------------------+
    only showing top 20 rows
    



```python
sdf.groupBy('symbol').count().sort('count', ascending=False).show(truncate=False)
```

    +-----------------------------------------------------+-----+
    |symbol                                               |count|
    +-----------------------------------------------------+-----+
    |window.document.cookie                               |3390 |
    |window.navigator.userAgent                           |1797 |
    |window.Storage.getItem                               |807  |
    |window.localStorage                                  |442  |
    |window.Storage.setItem                               |363  |
    |window.navigator.plugins[Shockwave Flash].description|238  |
    |window.sessionStorage                                |236  |
    |window.Storage.removeItem                            |185  |
    |window.name                                          |185  |
    |window.screen.colorDepth                             |166  |
    |window.navigator.appName                             |135  |
    |window.navigator.platform                            |120  |
    |window.navigator.language                            |96   |
    |window.navigator.plugins[Shockwave Flash].name       |90   |
    |window.Storage.length                                |78   |
    |window.navigator.appVersion                          |74   |
    |HTMLCanvasElement.width                              |53   |
    |window.Storage.key                                   |48   |
    |window.navigator.cookieEnabled                       |45   |
    |window.navigator.product                             |43   |
    +-----------------------------------------------------+-----+
    only showing top 20 rows
    

