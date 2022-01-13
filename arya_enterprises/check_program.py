"""
Program: Process ID get
Description:
Date of Creation: 06.01.2022
Author: Santosh Behera
Modifications:
MOD-000:        Any modifications can enlisted here with a proper modification token

"""

# import psutil
#
#
# for p in psutil.process_iter(attrs=['pid', 'name']):
#     print(p)
#     if p.info['name'] == "Python":
#         print("yes", (p.info['name']))
#     else:
#         # print("no process")
#         pass

# -------------------------------------------------------------------------------
# import psutil
# for pid in psutil.pids():
#     # print(pid)
#     p = psutil.Process(pid)
#     # print(p)
#     if p.name() == "pycharm" and len(p.cmdline()) > 1 and "crontab_cases.py" in p.cmdline()[1]:
#         print("running")
#     else:
#         pass


# -------------------------------------------------------------------------------
# import psutil
# import sys
# from subprocess import Popen
#
# for process in psutil.process_iter():
#     print(process)
#     if process.cmdline() == ['python', 'crontab_cases.py']:
#         sys.exit('Process found: exiting.')
#
# print('Process not found: starting it.')
# Popen(['python', 'your_script.py'])


# ----------------------------------------------------------------------
# import subprocess
#
# python_process = subprocess.check_output("ps -fA | grep python", shell=True)
# # python_process_1 = python_process.split("\n")
# print(python_process)
# p_id = python_process_1[1:10]  # ps ax | grep 'python x' | grep -v grep | awk '{print $1}'
# print(p_id)
# for process in python_process_1:
#     print(process)

# ------------------------------------------------------------
import psutil
import os
from crontab_cases import *
# pid_value = os.getpid()
# print(pid_value)

# pid = get_pid.pid_value
print(pid_value)

for p in psutil.process_iter(attrs=['pid', 'name', 'status']):
    # print(p)

    if 'Python' in p.info['name']:
        print(p.info['pid'], p.info['name'], p.info['status'])

# -----------------------------------------------------------
#
#
# import psutil
# import datetime
# import time
# from subprocess import Popen
#
# set_time = datetime.time(hour=22, minute=00)
#
# def findProcessIdByName(processName):
#     '''
#     Get a list of all the PIDs of a all the running process whose name contains
#     the given string processName
#     '''
#     listOfProcessObjects = []
#     # Iterate over the all the running process
#     for proc in psutil.process_iter():
#         try:
#             pinfo = proc.as_dict(attrs=['pid', 'name', 'create_time'])
#             # Check if process name contains the given name string.
#             if processName.lower() in pinfo['name'].lower():
#                 listOfProcessObjects.append(pinfo)
#         except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
#             pass
#     return listOfProcessObjects
#
# # Find PIDs od all the running instances of process that contains 'chrome' in it's name
# listOfProcessIds = findProcessIdByName('python')
# if len(listOfProcessIds) > 0:
#     print('Process Exists | PID and other details are')
#     for elem in listOfProcessIds:
#         processID = elem['pid']
#         processName = elem['name']
#         processCreationTime = time.strftime('%H:%M:%S', time.localtime(elem['create_time']))
#         print((processID, processName, processCreationTime))
#
#
# else:
#     print('No Running Process found with given text')
