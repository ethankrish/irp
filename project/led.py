import time
import RPi.GPIO as GPIO

POWERPIN = 23
MOTIONPIN = 4

def initialize():
    GPIO.setup(MOTIONPIN, GPIO.OUT)
    GPIO.setup(POWERPIN, GPIO.OUT)

def power_led(state):
    if state:
        GPIO.output(POWERPIN, GPIO.HIGH)
    else:
        GPIO.output(POWERPIN, GPIO.LOW)
	

def motion_led(state):
    if state:
        GPIO.output(MOTIONPIN, GPIO.HIGH)
    else:
        GPIO.output(MOTIONPIN, GPIO.LOW)

if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    initialize()
    delay = 0.5

    print("Testing led.py")
    power_led(True)
    time.sleep(delay)
    motion_led(True)
    time.sleep(delay)
    power_led(False)
    time.sleep(delay)
    motion_led(False)
    time.sleep(delay)
    GPIO.cleanup
