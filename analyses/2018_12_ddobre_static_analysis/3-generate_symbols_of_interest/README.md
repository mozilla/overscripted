# API Symbol extraction from JSON database:

Requires Mozilla's API list found on the [browser compatability data github](https://github.com/mdn/browser-compat-data/tree/master/api). For this reference, I've downloaded all of the json files into a directory called `api/`.

To run, configure the provided `config.ini` file. Make sure to specify both the directory of the api json files (found above) as well a list of those to generate symbol lists for. Run with:
```
$ ./process_APIs.py
```

Program will run through the specified .json files, extracting methods/symbols, and then checking if these methods/symbols also exist as .json files in the json directory. If they do (and they haven't already been parsed), then program will also check through those files.

Spits out a json file with a user specified name, with keys corresponding to the original interface, and values containing the lists of the corresponding symbols and methods.
