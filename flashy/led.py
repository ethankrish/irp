#!/usr/bin/env python

"""led.py: Turns on an and off two LEDs"""

__author__ = "Ethan Ramchandani"

import RPi.GPIO as GPIO
import time

waittime = 0.3
portnum = 23
portnum2 = 4

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(portnum, GPIO.OUT)
GPIO.setup(portnum2, GPIO.OUT)
try:
    while True:
        print "Led on"
        GPIO.output(portnum, GPIO.HIGH)
        GPIO.output(portnum2, GPIO.LOW)
        time.sleep(waittime)
        print "Led off"
        GPIO.output(portnum, GPIO.LOW)
        GPIO.output(portnum2, GPIO.HIGH)
        time.sleep(waittime)
except:
    GPIO.cleanup()
