#!/usr/bin/python3
def number_keys(a_dictionary):
    num = 0
    lst_keys = list(a_dictionary.keys())

    for i in lst_keys:
        num += 1

    return (num)
