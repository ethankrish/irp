import time
from datetime import datetime

# write a function that opens 
# /home/pi/motiondata.txt
# if it exists then it should write the 
# current date and time to the end and close it
# if it doesn't exist it should create and 
# write to the current date and time to the end
# and close it.
# it should write date and time up seconds.

def recordnow():
    s = datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S\n")
    file = open("/home/pi/research/project/motiondata.txt", 'a')
    file.write(s)
    file.close()


if __name__ == "__main__":
    recordnow()
    time.sleep(1)
    recordnow()
