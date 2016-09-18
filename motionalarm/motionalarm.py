import sys
import RPi.GPIO as GPIO
from pygame import mixer
import time

motionpin=18

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


def main_loop():
    oldvalue=-1
    while True:
        i=GPIO.input(motionpin)
        if i != oldvalue:
            if i==0:
                motion_stopped()
            else:
                motion_detected()
        time.sleep(0.1)
        oldvalue = i



initialize()
main_loop()
