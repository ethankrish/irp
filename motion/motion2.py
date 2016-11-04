#!/usr/bin/env python

import RPi.GPIO as GPIO
import time


"""motion2.py tells you when motion is detected and when it is clear"""

__author__ = "Ethan Ramchandani"

motionpin=18

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(motionpin, GPIO.IN)

oldvalue=-1
try:
    while True:
        i=GPIO.input(motionpin)
        if i != oldvalue:
            if i==0:
                print "clear", i
            else:
                print "intruder!", i
        time.sleep(0.1)
        oldvalue = i
except:
    GPIO.cleanup()
