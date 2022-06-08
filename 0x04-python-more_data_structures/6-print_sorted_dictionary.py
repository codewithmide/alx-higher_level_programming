#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sort_dic = []
    for i in a_dictionary:
        sort_dic.append(i)
    sort_dic.sort()
    for i in sort_dic:
        print('{}: {}'.format(i, a_dictionary[i]))
