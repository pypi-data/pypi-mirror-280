---
title: README
---

# Synopsis

A file adapter for the [Requests](https://docs.python-requests.org/en/latest/index.html) library. This adapter is similar to and inspired by [Requests-File](https://github.com/dashea/requests-file) but with the following changes:

* HEAD requests return a response without content instead of opening the file.
* The following HTTP response headers are set for regular files:
    - Content-Length (always)
    - Last-Modified (always)
    - Content-Type (if successfully detected by the mimetypes package)
    - Content-Encoding (if successfully detected by the mimetypes package)
* The request supports URI hosts that resolve to the localhost or any local IP address.
* A convenience function is provided to get a requests.Session object with the provided file adapter already mounted.

# Links

[insert: links]: #

## GitLab

* [Homepage](https://gitlab.inria.fr/jrye/requests-file-adapter)
* [Source](https://gitlab.inria.fr/jrye/requests-file-adapter.git)
* [Documentation](https://jrye.gitlabpages.inria.fr/requests-file-adapter)
* [Issues](https://gitlab.inria.fr/jrye/requests-file-adapter/-/issues)
* [GitLab package registry](https://gitlab.inria.fr/jrye/requests-file-adapter/-/packages)

## Other Repositories

* [Python Package Index](https://pypi.org/project/Requests-File-Adapter/)

[/insert: links]: #

# Installation

Install the `requests_file_adapter` package with your Python package manager, e.g.

~~~
pip install requests_file_adapter
~~~

# Usage

Using the `get_session` function:

~~~python
import pathlib
from requests_file_adapter import get_session

path = pathlib.Path("example.txt").resolve()
uri = path.as_uri

session = get_session()
resp = session.get(uri)
for header, value in resp.headers.items():
    print(header, value)
print(header.content)
~~~

Alternatively, create the session without using the `get_session` function:

~~~python
import requests
from requests_file_adapter import FileAdapter

session = requests.Session()
session.mount("file://", FileAdapter())

# ...
~~~
