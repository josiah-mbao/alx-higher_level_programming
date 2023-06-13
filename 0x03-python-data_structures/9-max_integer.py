#!/usr/bin/python3
# 9-max_integer.py


def max_integer(my_list=[]):
    """Find the biggest int of a list."""
    if len(my_list) == 0:
        return (None)

    max_so_far = my_list[0]
    for i in range(len(my_list)):
        if my_list[i] > max_so_far:
            max_so_far = my_list[i]

    return (big)
