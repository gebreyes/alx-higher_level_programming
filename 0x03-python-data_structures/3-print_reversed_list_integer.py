#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    if my_list:
        # Syntax: reversed_list = systems[start:stop:step]
        my_list = my_list[::-1]
        for x in range(len(my_list)):
            print("{:d}".format(my_list[x]))
