import time 
import os
import sys
from datetime import time
import datetime
# file = open("file.txt", 'w+')


# while True:
# 	with open("file.txt", 'w') as f:

# 		print("After 3 seconds", file=f)
# 		time.sleep(3)

# while True:
# 	f = open('file.txt', 'w')
# 	print("hiiiiiiiii", file=f, end=" ")
# 	time.sleep(3)
while (True):
	now = datetime.datetime.now()
	# print(now)
	with open('prime.txt', 'a') as prime_file:
	    for num in range(2, 1000000000000):
	        prime = True
	        for i in range(2, num):
	            if (num % i == 0):
	                prime = False
	                break # <- Also added this. You should stop iterating once you know the number is not prime
	        if prime:
	            print(num)
	            prime_file.write('{}\n'.format(num))
	    if now.hour == 16 and now.minute == 24:
        print("close")
        sys.exit()
			