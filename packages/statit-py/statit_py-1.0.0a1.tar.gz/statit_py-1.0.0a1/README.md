# statit_py
This package is a set of utilities for [Statit](https://gostatit.com), including API access and some data manipulation utilities.

## Installation

To install the current release:

```
$ pip install statit_py
```

## Quick usage

To use the Statit REST API methods, first authenthicate yourself with your username and API token (see [Signing-in](https://help.gostatit.com/excel/signin/#authentication)):

```py
import statit_py

statitAPI = statit_py.coreAPI('YOUR_USERNAME', 'YOUR_API_KEY')
```

`GET`, `LIST` and `DELETE` actions for collections and series are available in reference-by-ID format:

```py
data = api.getSerie('SERIE-ID')
```

Alongside with the remaining `PUT`, `UPDATE` and `BATCHPUT` actions, they are also available in standard JSON request format:

```py
api.putSerieJSON({
    'id': 'SERIE_ID',
    ...
})
```

For the full list of methods and their detailed arguments, see the [Python Documentation]().






