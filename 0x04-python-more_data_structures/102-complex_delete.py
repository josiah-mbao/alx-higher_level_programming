#!/usr/bin/python3
def complex_delete(a_dict, value):
    list_keys = list(a_dict.keys())

    for value_dic in list_keys:
        if value == a_dict.get(value_dic):
            del a_dict[value_dic]

    return (a_dict)
