import sys
import os.path
import traceback
import logging

import RPi.GPIO as GPIO
from pygame import mixer
import time
import picamera

import led
from email_alert import send_email
import config

MOTIONPIN=18
MYDIR = os.path.dirname(os.path.realpath(__file__))


def initialize_logging():
    logging.basicConfig(filename=os.path.join("/home/pi/irp.log"),
            level=logging.DEBUG,
            format="%(asctime)s:%(levelname)s:%(message)s"
            )

def take_picture():
    with open(os.path.join(MYDIR, 'image.jpg'), 'wb') as image_file:
        with picamera.PiCamera() as camera:
            camera.capture(image_file)


def initialize():
    config.initialize()
    mixer.init()
    mixer.music.load(os.path.join(MYDIR, "intruder2.mp3"))
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(MOTIONPIN, GPIO.IN)
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
    send_email(config.get_value('alert_destination'),
               'Intruder Alert',
               'Motion alarm triggered',
               os.path.join(MYDIR, 'image.jpg'))

def uninitialize():
    try:
        GPIO.cleanup()
        mixer.quit()
        led.power_led(False)
    except:
        pass #swallow all exceptions on uninitialize


def main_loop():
    oldvalue=-1
    while True:
        i=GPIO.input(MOTIONPIN)
        # only react to changes
        if i != oldvalue:
            if i==0:
                motion_stopped()
            else:
                motion_detected()
        time.sleep(0.1)
        oldvalue = i


try:
    initialize_logging()
    initialize()
    main_loop()
except:
    logging.exception("Got exception")
    traceback.print_exc(file=sys.stdout)
    uninitialize()
