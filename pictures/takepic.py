#!/usr/bin/env python

import picamera

"""takepic.py takes a picture and saves it"""

__author__ = "Ethan Ramchandani"

camera = picamera.PiCamera()
camera.capture('image2.jpg')