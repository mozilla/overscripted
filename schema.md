* __call_stack:__
    * __Type:__ String
    * __Description:__ The call stack at the point when the function is called. The output is in the format: (function_name)(@)(javascript_source_file)(:)(line_number)(column_number)(new_line_character)
    * __Example:__ 
    ```
    jQuery.cookie@https://cdn.livechatinc.com/js/embedded.20171215135707.js:5:8393\nStore</s.get@https://cdn.livechatinc.com/js/embedded.20171215135707.js:8:3323\nStore</</s[p]@https://cdn.livechatinc.com/js/embedded.20171215135707.js:8:3746\nWindowsCommunicator.prototype.startCheckingForMainWindow/e<@https://cdn.livechatinc.com/js/embedded.20171215135707.js:10:11730
    ```
* __crawl_id:__
    * __Type:__ Integer
    * __Description:__ Crawl_id appears to be the value 1 for all json files. It is possible this field was not used when generating the data using the crawler.
    * __Example:__ 1
* __func_name:__
    * __Type:__ String
    * __Description:__ The name of the javascript function. Due to obfuscation the functions are often nonsensical and thus can be thought of as tokens. Anonymous functions will not have a name and the value will be an empty string.
    * __Examples:__ 
    ```
    ""
    a<4k
    getName
    ```
* __in_iframe:__
    * __Type:__ boolean
    * __Description:__ in_iframe is a boolean that indicates that the javascript code was run inside of an iframe. This is new functionality that was added ontop of the origional OpenWPM repository.
* __location:__
    * __Type:__ string
    * __Description:__ The url of the file that was being crawled to generate the json file. For iFrame resources, the location will be different that the parent url where the iFrame was encountered. For example, if Parent.html contains iFrame.html, iFrame.html is added inside an <iframe> tag. Inside iFrame.html a line of javascript such as: alert("window.location") is used to assert the location of content. When openWPM queries content that is inside iFrame.html which is found on Parent.html the location of the content is reported as: iFrame.html not Parent.html. Due to the paralellization of the crawl, the iFrame content can not be associated with the parent site on which it was encountered, only the __in_iframe__ filed can indicate whether the content was executed inside an iFrame or not. All objects in a json file that were accessed from the crawled page outside of an iFrame should have the same location value. The url can be for any type of file such as .html, .js or have no file extension.
    * __Examples:__ 
    ```
    https://www.dresslily.com/bottom-c-36.html
    http://www.vidalfrance.com/component/forme/?fid=2
    ```
* __operation:__
    * __Type:__ string
    * __Description:__ Corresponds to the "symbol" field. Operation is a call if the symbol is a method. Get/set operations get and set symbols that are properties with values. 
    * __Possible Values:__ get, call, set
* __script_col:__
    * __Type:__ string
    * __Description:__  The column in the `script_line` where the function call starts. Note: currently some string do not contain numbers, but instead they contain urls such as the example bellow.
    * __Examples:__ 
    ```
    57
    211
    //hdjs.hiido.com/hiido_internal.js?siteid=mhssj
    ```
* __script_line:__
    * __Type:__ string
    * __Description:__ The line in the file, indicated in the above `location` element, where the function call is located. Note: Currently some strings do not contain numbers, but instead they contain the protocol identifier for a url, such as in the example bellow.
    * __Examples:__ 
    ```
    12
    129
    http
    https
    ```
* __script_loc_eval:__
    * __Type:__ string
    * __Description:__ If a function call is generated using the `eval()` function, or is created using `new Function()`, then the "script_loc_eval" value will be set. For example `eval("console.log('my message')")` or `var log = new Function("message", "console.log(message)"); log("my message");` will both cause the "script_loc_evel" value be set when the function calls were collected. The format of "scipt_loc_eval" is: (line) (LINE_NUMBER) (>) (eval | Function) and can be repeated multiple times.  Additional information on how the eval line number is generated can be found at the bottom of the [MDN page](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error/Stack) which discusses the `Error` objects `stack` property. The "script_loc_eval" element is generated from this stack property.
    * __Examples:__ 
    ```
    ""
    line 2 > eval
    line 70 > Function
    line 140 > eval line 232 > Function
    line 1 > Function line 1 > eval line 1 > eval
    ```
* __script_url:__
    * __Type:__ string
    * __Description:__ The url of the file where the javascript function call was run.  This may be the same value at "location", or it may be an external web url that was loaded into the website with the use of the `<script>` tag. 
    * __Examples:__ 
    ```
    http://www.google-analytics.com/analytics.js
    http://ajax.googleapis.com/ajax/libs/jquery/1.6/jquery.min.js
    http://pw.myersinfosys.com/javascripts/jquery-cookie.js?rwdv2
    https://g.alicdn.com/alilog/oneplus/blk.html#coid=52m7EjiWaj8CASPiP1nwaYXC&noid=&grd=n
    inline-cloudflare-rocketloader-executed-3.js
    /_/scs/shopping-verified-reviews-static/_/js/k=boq-shopping-verified-reviews.VerifiedReviewsBadgeUi.en_US.-JtwBcVsOWQ.O/m=_b,_tp/rt=j/d=1/excm=badgeview,_b,_tp/ed=1/rs=AC8lLkQbsBabKLQ4BgeJxo8BUz31aigxHA
    blob:http://nadgames.com/3334aa5f-24af-4c2f-9e52-fe196a0068b6
    ```
* __symbol:__
    * __Type:__ string
    * __Description:__ Either a Web API interface property (with a value) or method (which may take args as listed in "arguments" field). Symbol corresponds to "operation" field.
    * __Examples:__ 
    ``` 
    window.Storage.getItem 
    window.navigator.userAgent
    CanvasRenderingContext2D.textBaseline
    ```
* __time_stamp:__
    * __Type:__ string
    * __Description:__ The timestamp of when the javascript function information was collected. The timestamp is collected using Javascripts Date.now() function.  It is in the format YYYY-MM-DDTHH:mm:ss.sssZ. 
      * YYYY-MM-DD is the: year-month-day. 
      * "T" is a delimiter to seperate the two sections. 
      * HH:mm:ss.sss represents the: hours, minutes, seconds, and milliseconds. 
      * Z is optional and denotes the time zone. Z represents the time zone UTC+0.
    * __Examples:__ 
    ```
    2017-12-16T00:17:37.973Z
    2017-12-16T00:24:09.355Z
    2017-12-16T08:10:24.749Z
    ```
* __value:__
    * __Type:__ string
    * __Description:__ The value that the function returned.
    * __Examples:__
    ```
    ""
    {}
    Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0
    \_ga=GA1.2.1076416180.1513383458; \_gid=GA1.2.1940452730.1513383458
    {"name": "example", "Browser": "Mozilla/5.0"}
    ```
* __arguments:__ 
	* __Type:__ object
	* __Description:__ Optional property which lists the arguments taken by the method in "symbol" field. 
	* __Examples:__ 
    ``` 
    {\"0\":\"liveAgentPc\"}
    {\"0\":\"liveAgentPage_0\",\"1\":\"http://www.alamy.com/help/what-is-model-release-property-release.aspx\"}
    ```
