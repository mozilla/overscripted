# Analyze Syntax Tree Counts

This portion performs the actual counting of API symbol calls by generating an abstract syntax tree (AST) and walking through it (breadth-first) to extract symbol information. The AST generation is performed by [Esprima](https://github.com/Kronuz/esprima-python).

There are two scripts. `async_tree_explorer.py` uses the parameters specified in `config.ini` to asynchronously generate symbol counts for all files within a directory. Depending on your machine, this may take a long time (10000 files took about 12 hours in one sample using 16 workers). There isn't a significant memory overhead, so depending on the size of your dataset, 16-32GB of RAM should be enough. The is a pandas dataframe with the schema: `['filename', 'symbol_1' , ... , 'symbol_n']`. This results in NaN values for scrips that do not have a symbol call that others do. The benefit of this is that one can analyze specific symbols.

`single_tree_explorer.py` performs the same analysis as `async_tree_explorer.py` on a single file specified by the user at runtime. Runs with:
```
$ ./single_tree_explorer.py <path/to/api_list> <path/to/js_file>
```
This generates two outputs in `output_data`. `symbol_counts.json` is the output the count of bottom level calls, for example `window.location.href` would be counted as `href`. `extended_symbol_counts.json` would attempt to find the whole symbol `window.location.href`. There are limitations to this however. If the calls were broken up over several different functions, the AST has no way of recovering that information, so you might be left with `location.href`. Depending on the symbol, it might be possible to infer the parent APIs, but there are many cases of conflict which makes this not guaranteed. Furthermore, if the script is heavily obfuscated, then this approach will almost certainly fail. 

The cases this script looks for are `MemberExpressions`, `CallExpressions`, and `object`s within either of the expressions.

Looking at some examples, the JavaScript line
```js
if ((new RegExp("WebKit")).test(navigator.userAgent))
```
parses out to:
```json
"type": "IfStatement",
"test": {
        "type": "CallExpression",
        "callee": {
                "type": "MemberExpression",
                "computed": false,
                "object": {
                        "type": "NewExpression",
                        "callee": {
                                "type": "Identifier",
                                "name": "RegExp"
                        },
                        "arguments": [
                        {
                                "type": "Literal",
                                "value": "WebKit",
                                "raw": "\"WebKit\""
                        }
                        ]
                },
                "property": {
                        "type": "Identifier",
                        "name": "test"
                }
        },
        "arguments": [
        {
                "type": "MemberExpression",
                "computed": false,
                "object": {
                        "type": "Identifier",
                        "name": "navigator"
                },
                "property": {
                        "type": "Identifier",
                        "name": "userAgent"
                }
        }
        ]
},
...
```
The syntax tree walker will focus on nodes with the type `MemberExpression` or `CallExpression`. Focusing on the node which has the appropriate type:
```json
{
        "type": "MemberExpression",
        "computed": false,
        "object": {
                "type": "Identifier",
                "name": "navigator"
        },
        "property": {
                "type": "Identifier",
                "name": "userAgent"
        }
}
```
The script first grabs the `property.name` parameter of this node, which is `userAgent`. The value is then compared to the list of symbols fed in, and if it does not exist in that list, this node is ignored. This would be the "outermost" symbol call, so this value is set to be the current output string (`output = userAgent`). The algorithm now recursively checks for objects in the node and repeats the first part of checking for types and properties. In this case, the object type is `Identifier`, so this this is the bottom of this branch and this value is prepended before the final value, i.e.  `tmp = navigator.userAgent`. Note that the object's type might have been `MemberExpression` or `CallExpression`, in which case `property.name` is prepended to the output, and then another `object` check is done (until the object is of type `Identifier`).

In the case of `CallExpression`, the same logic applies but instead of looking for `node.property.name`, we must look for `node.callee.name`. For example:
```json
"type": "CallExpression",
"callee": {
        "type": "Identifier",
        "name": "setInterval"
},
```
where `setInterval` is the symbol extracted.

Note that this approach is vulnerable to prepending nodes which share names with valid symbols in the symbol list. This is largely the case for single character object names, such as `d.userAgent`, where `d` is a valid symbol in `DOMMatrixReadOnly`. This is mitigated by assuming that parent objects are unlikely to be of length 1 or 2, so any parents which have only one or two characters are discarded. The only vulnerable two character values would be `id`, `go`, `as`, `ch`, and `db` (using the provided master list).

