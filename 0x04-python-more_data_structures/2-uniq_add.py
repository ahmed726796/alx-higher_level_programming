#!/usr/bin/python3
def uniq_add(my_list=[]):
    n = set(my_list)
    s = 0
    for i in n:
        s += i
    return (s)
