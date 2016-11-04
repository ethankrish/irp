#!/usr/bin/env python

# found on stackoverflow

import urllib2

"""internetcheck.py checks for internet by trying to connect to google"""

__author__ = "Ethan Ramchandani"


def internet_on():
    try:
        response=urllib2.urlopen('http://www.google.com', timeout=1)
        return True
    except urllib2.URLError as err: pass
    return False


if __name__ == '__main__':
    print(internet_on())
