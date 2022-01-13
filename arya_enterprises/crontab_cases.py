# Starting from  12 AM to 11.55 PM  using crontab for shutter detection

# 0 12 * * * (full path of python virtual environment) (full path of python file )

# Starting from 9 PM everyday using crontab

# * 21 * * * (full path of python virtual environment) (full path of python file )

import sys
from datetime import time
import datetime
import cv2
import psutil
import os

# def get_pid():
# pid_value = os.getpid()
# print(pid_value)
    # return pid_value

# For webcam input = 0
# vid = cv2.VideoCapture(0)

# For video file input = relative file / absoulute video file path with extension (e.g ./video/crowd.mp4)
vid = cv2.VideoCapture("./video/crowd.mp4")

while (True):
    now = datetime.datetime.now()

    ret, frame = vid.read()
    cv2.imshow('frame', frame)
    print("[INFO] Running Mode on")
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    if now.hour == 17 and now.minute == 52:
        print("close")
        sys.exit()

# vid.release()
# cv2.destroyAllWindows()
