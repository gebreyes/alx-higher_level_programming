#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num_str = repr(number)
last = int(num_str[-1])
if last>5:
    print(f"The last digit of {num_str} is {last} and is greater than 5")
elif last == 0:
    print(f"The last digit of {num_str} is {last} and is 0")
elif last < 6 and last !=0:
    print(f"The last digit of {num_str} is {last} and is less than 6 and not 0")
else:
    pass
