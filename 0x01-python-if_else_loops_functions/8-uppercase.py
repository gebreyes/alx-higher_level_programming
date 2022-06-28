#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) >= 65 and ord(i) <= 96:
            i = chr(ord(i))
        else:
            i = chr(ord(i) - 32)
        print("{}".format(i), end="")
    print("")
