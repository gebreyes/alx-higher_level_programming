#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    if idx < 0:
        return my_list
    elif idx >= len(my_list):
        return my_list
    else:
        for x in range(len(my_list)):
            my_list.pop(idx)
            my_list.append(idx, element)
        return my_list