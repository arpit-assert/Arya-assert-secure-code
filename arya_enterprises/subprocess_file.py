"""
Program: Rerun the code in a given time range
Description:
Date of Creation: 06.01.2022
Author: Santosh Behera
Modifications:
MOD-000:        Any modifications can enlisted here with a proper modification token

"""

import subprocess
from subprocess import Popen
import datetime

start = datetime.time(17, 00, 0)
end = datetime.time(17, 52, 0)
current = datetime.datetime.now().time()

print(f"starting time {start} and ending time {end} and cuurent time {current}")
print(start <= current <= end)
while (True):
    if start <= current and current <= end:

        current = datetime.datetime.now().time()

        cmd = ['pgrep -f .*python .crontab_cases.py']
        process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        my_pid, err = process.communicate()
        print(my_pid)
        # if start <= current <= end:
        # while (True):
        if len(my_pid.splitlines()) > 0:
            print("Running")
        else:
            print("Not Running")
            Popen(['python', 'crontab_cases.py'])

    else:
        print("Not in specific time range")
        break

