#!/usr/bin/python3
def search_replace(my_list, search, replace):
    n_list = []
    for num in range(len(my_list)):
        n_list.append(my_list[num])
        if my_list[num] == search:
            n_list[num] = replace
    return n_list
