#!/usr/bin/python3
def simple_delete(a_dict, key=""):
    if a_dict.get(key) is not None:
        del a_dict[key]
    return (a_dict)
