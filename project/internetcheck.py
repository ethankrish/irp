# found on stackoverflow

import urllib2

def internet_on():
    try:
        response=urllib2.urlopen('http://www.google.com', timeout=1)
        return True
    except urllib2.URLError as err: pass
    return False


if __name__ == '__main__':
    print(internet_on())
