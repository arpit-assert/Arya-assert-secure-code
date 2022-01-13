import subprocess
from subprocess import Popen
from subprocess import call
import datetime
import os
import gc

start = datetime.time(11, 00, 0)
end = datetime.time(11, 12, 0)
current = datetime.datetime.now().time()

print(f"starting time {start} and ending time {end} and cuurent time {current}")
# print(start <= current <= end)
while (True):
    current = datetime.datetime.now().time()
    try:

        if start <= current and current <= end:

            

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
                # Popen(['python', 'crontab_cases.py'])
                # call(["python", "crontab_cases.py"])
                # os.system("python crontab_cases.py")

                # For permission related issue use : chmod +wrx file_name(script_file.sh)
                # subprocess.Popen(["./script_file.sh"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                call("./script_file.sh", shell=True)
                # os.system("sh script_file.sh")
                # subprocess.run(['./script_file.sh'])

        else:
            print("Not in specific time range")
            break
    except Exception as e:
        print(e)

gc.collect()
