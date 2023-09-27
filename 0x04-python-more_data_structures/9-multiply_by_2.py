#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    k = a_dictionary.copy()
    key_l = list(k.keys())

    for i in key_l:
        k[i] *= 2

    return k
