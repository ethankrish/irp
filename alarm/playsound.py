# Gobo needs to write code here to play intruder1.mp3
# on the pi
from pygame import mixer
import time

mixer.init()
mixer.music.load('/home/pi/research/alarm/intruder1.mp3')
mixer.music.play()

time.sleep(10)

mixer.music.stop()
