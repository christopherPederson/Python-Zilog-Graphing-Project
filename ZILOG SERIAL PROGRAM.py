import serial #serial communication from board
import time #real time library
import matplotlib.pyplot as plt #graphing and display library

#define serial parameters
serialData = serial.Serial('COM6', 57600, timeout=1)

#stores time stamps for each motion event
motionEventAry = []

#stores seperation of each motion event in seconds
motionEventSeperationAry = []

#time stamp of most recent event
lastMotionEvent = time.time()

currentMotionEvent = 0

#setting experiment time limit currently set to 1 minute
timeLimit = lastMotionEvent + 60

while time.time() < timeLimit:
    data = serialData.readline()

# Decode bytes to string
    if isinstance(data, bytes):
        data = data.decode('utf-8')

        if "Motion Detected" in data:
            currentMotionEvent = time.time()
            motionEventSeperationAry.append(currentMotionEvent - lastMotionEvent)
            motionEventAry.append(currentMotionEvent)
            lastMotionEvent = currentMotionEvent

# plot and display data
plt.plot(motionEventSeperationAry)
plt.show()
