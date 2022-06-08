#!/usr/bin/python3
def best_score(a_dictionary):
    name = ""
    score = 0
    if not a_dictionary:
        return None
    else:
        for key in a_dictionary:
            if a_dictionary[key] > score:
                score = a_dictionary[key]
                name = key
    return name
