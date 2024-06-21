python-apereocla
================

[![Build Status](https://github.com/lkiesow/python-apereocla/actions/workflows/test.yml/badge.svg)](https://github.com/lkiesow/python-apereocla/actions/workflows/test.yml)

This is a simple python library to parse and access the Apereo Foundation's
lists include those who have submitted Apereo Foundation CLAs, as well as those
who had previously submitted CLAs with Jasig or Sakai.

The data is retrieved from the official lists at:

> http://licensing.apereo.org/

This library offers access to the lists of ICLAs, CCLAs as well as the list of
Github user names associated with ICLAs.


Usage
-----

Install with

```
❯ pip install apereocla
```

Run the tool with:

```
❯ apereocla           
Usage: /home/lars/.local/bin/apereocla [ -g github_user | -n name | -c company ]
```

For example, to check if the GitHub user `lkiesow` submitted an ICLA, run:
```
❯ apereocla -g lkiesow
```

Library
-------

The library consists of three methods:

- `github_users()` returns a generator for the lists of Github usernames
  associated with completed ICLAs.
- `icla()` returns a generator for the lists of persons/names associated with
  completed ICLAs.
- `ccla()` returns a generator for the lists of organization names associated
  with completed CCLAs.


Example
-------

Print list of all Github usernames with a completed Apereo ICLA:

```python
from apereocla import github_users

for user in github_users():
    print(user)
```

Running this script yields:
```bash
% python list-github-user-with-icla.py
Aaron-G-9
acspike
adrianmticarum
alejandrogj
…
```
