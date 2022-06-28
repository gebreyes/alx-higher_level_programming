#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0:
    print(f"{number:2d} is positive")
elif number < 0:
    print(f"{number:2d} is negative")
else:
    print(f"{number:2d} is zero")
