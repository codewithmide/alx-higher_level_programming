#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    initial = []
    for i in set_1:
        initial.append(i)
    related = [x for x in initial if x in set_2]
    for i in set_2:
        initial.append(i)
    result = [x for x in initial if x not in related]
    return result
