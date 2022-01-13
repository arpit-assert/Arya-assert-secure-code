# Starting from  12 AM to 11.55 PM  using crontab for shutter detection

# 0 12 * * * (full path of python virtual environment) (full path of python file ) >> ~/cron.log

# Starting from 9 PM everyday using crontab

# * 21 * * * (full path of python virtual environment) (full path of python file ) >> ~/cron.log

import sys
from datetime import time
import datetime
import cv2
import psutil
import os

# def get_pid():
pid_value = os.getpid()
print(pid_value)
    # return pid_value

vid = cv2.VideoCapture("./video/crowd.mp4")
# vid = cv2.VideoCapture(0)

while (True):
    now = datetime.datetime.now()

    ret, frame = vid.read()
    cv2.imshow('frame', frame)
    print("[INFO] Running Mode on")
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    if now.hour == 20 and now.minute == 50:
        print("close")
        sys.exit()

vid.release()
cv2.destroyAllWindows()
