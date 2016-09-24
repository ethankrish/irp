import sys
import traceback
import RPi.GPIO as GPIO
from pygame import mixer
import time
import picamera
import led

motionpin=18

def take_picture():
    with open('image.jpg', 'wb') as image_file:
        with picamera.PiCamera() as camera:
            camera.capture(image_file)


def initialize():
    mixer.init()
    mixer.music.load("/home/pi/research/motionalarm/intruder2.mp3")
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(motionpin, GPIO.IN)
    led.initialize()
    led.power_led(True)

def motion_stopped():
    print "clear"
    led.motion_led(False)
    mixer.music.stop()

def motion_detected():
    print "intruder!"
    led.motion_led(True)
    mixer.music.play()
    take_picture()

def uninitialize():
    GPIO.cleanup()
    mixer.quit()
    led.power_led(False)


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


try:
    initialize()
    main_loop()
except: 
    uninitialize()
    traceback.print_exc(file=sys.stdout)
