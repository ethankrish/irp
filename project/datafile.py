#!/usr/bin/env python

import time
from datetime import datetime

"""datafile.py: Logs date and time to a motiondata.txt"""

__author__ = "Ethan Ramchandani"



def recordnow():
    """
    This function records the current date and time in /home/pi/motiondata.txt
    """
    s = datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S\n")
    file = open("/home/pi/research/project/motiondata.txt", 'a')
    file.write(s)
    file.close()


if __name__ == "__main__":
    recordnow()
    time.sleep(1)
    recordnow()
