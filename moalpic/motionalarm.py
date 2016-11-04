# !/usr/bin/env python

import sys
import traceback
import RPi.GPIO as GPIO
from pygame import mixer
import time
import picamera


"""motionalarm.py plays a sound when motion is detected"""

__author__ = "Ethan Ramchandani"

motionpin = 18


def take_picture():
    camera = picamera.PiCamera()
    camera.capture('image.jpg')


def initialize():
    mixer.init()
    mixer.music.load("/home/pi/research/motionalarm/intruder2.mp3")

    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(motionpin, GPIO.IN)


def motion_stopped():
    print "clear"
    mixer.music.stop()


def motion_detected():
    print "intruder!"
    mixer.music.play()
    take_picture()


def uninitialize():
    GPIO.cleanup()
    mixer.quit()


def main_loop():
    oldvalue = -1
    while True:
        i = GPIO.input(motionpin)
        if i != oldvalue:
            if i == 0:
                motion_stopped()
            else:
                motion_detected()
        time.sleep(0.1)
        oldvalue = i


try:
    initialize()
    main_loop()
except:
    uninitialize()
    traceback.print_exc(file=sys.stdout)
