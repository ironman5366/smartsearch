[![PyPI version](https://badge.fury.io/py/smartsearch.svg)](https://badge.fury.io/py/smartsearch)  [![Build Status](https://travis-ci.org/ironman5366/smartsearch.svg?branch=master)](https://travis-ci.org/ironman5366/smartsearch)
# Smart search
## Installation
`pip install smartsearch`
## Basic usage
Start by passing a wolframalpha api key to searcher.Searcher

Search can be used without API keys, but any clients that require api keys and are not passed them will be disabled
```python
import search

# Define an API key for wolframalpha
key_data = {
    "wolfram": "my-wolfram-key"
}

# Instantiate a searcher instance
searcher = search.Searcher(keys=key_data)

# Make a query to the searcher
searcher.query("What's the meaning of life?")
# "42 (according to the book The Hitchhiker's Guide to the Galaxy, by Douglas Adams)"
searcher.query("Who is barack obama?")
# "Barack Hussein Obama II (US:  bə-RAHK hoo-SAYN oh-BAH-mə; born August 4, 1961) is an American politician who served as the 44th President of the United States from 2009 to 2017. He is the first African American to have served as president. (https://en.wikipedia.org/wiki/Barack_Obama)"
```

## Saving configurations
```python
searcher.save("search.conf")
```

## Loading a configuration
```python
import search

searcher = search.Searcher(conf_file="search.conf")
```

## Clients
    - Wolfram: Queries wolframalpha to try to find a direct answer to a query
    - Google: Does a google search of a query. If a wikipedia article is found in the first 4 urls on Google, use the wikipedia module to read the article. Otherwise, try to parse the first link from google trying first a complex approach with newspaper, and then falling back to a more basic solution with bs4.
