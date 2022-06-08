#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = {}
    for dict in a_dictionary:
        new_dict[dict] = a_dictionary[dict] * 2
    return new_dict
