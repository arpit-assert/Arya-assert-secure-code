import time
import sys
from datetime import time
import datetime

with open('prime.txt', 'a') as prime_file:

        for num in range(2, 1000000000000):
            while (True):
                print("inside while")
                now = datetime.datetime.now()
                print(now)
                if now.hour == 17 and now.minute == 18:
                    print("close")
                    sys.exit()
                prime = True
                for i in range(2, num):
                    if (num % i == 0):
                        prime = False
                        break  # <- Also added this. You should stop iterating once you know the number is not prime
                if prime:
                    print(num)
                    prime_file.write('{}\n'.format(num))
