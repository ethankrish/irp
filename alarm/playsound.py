# !/usr/bin/env python
from pygame import mixer
import time

"""playsound.py: Testing pygame to see if we can play an mp3"""

__author__ = "Ethan Ramchandani"

mixer.init()
mixer.music.load('/home/pi/research/alarm/intruder1.mp3')
mixer.music.play()

time.sleep(10)

mixer.music.stop()
