# The Problem
Your team is tasked with listing out music festival data in a particular manner: at the top level, it should show the band record label, below that it should list out all bands under their management, and below that it should display which festivals they've attended, if any. All entries should be sorted alphabetically.

The data is provided to you via an API by another team; they assure you all the data is available but it's in a different format and provide you with the Swagger documentation needed to get started.

Use this API as is to output the format specified above in console


### Prerequisites

You need to have python 3.6 and tox installed in order to run this program and tests

```
pip install tox
```

### Installing program into your machine

Run `tox`

## Running program

```
tox -e music
```

## Running unit tests

```
tox
```

## Example input of program (using api)
```
[
    {
        "name": "music festival 1",
        "bands": [
        {
            "name": "band 1",
            "recordLabel": "record label 1"
        },
        {
            "name": "band 2",
            "recordLabel": "record label 1"
        },
        {
            "name": "band 3",
            "recordLabel": "record label 2"
        }
        ]
    },
]
```
## Example output of program

```
"record label 1"
    "band 1"
        "music festival 1"
    "band 2"
        "music festival 1"
"record label 2"
    "band 3"
        "music festival 1"
```
## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags).

## Authors

* **Sourabh Kumar**