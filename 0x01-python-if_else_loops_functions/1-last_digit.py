#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num_str = repr(number)
last = int(num_str[-1])
if last>5:
    print("The last digit of {} is {} and is greater than 5".format(num_str, last))
elif last == 0:
    print("The last digit of {} is {} and is 0".format(num_str, last))
elif last < 6 and last !=0:
    print("The last digit of {} is {} and is less than 6 and not 0".format(num_str, last)
