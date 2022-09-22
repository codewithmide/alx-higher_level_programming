#!/usr/bin/python3
"""
    Write a function that finds a peak in a list of unsorted integers.
"""


def find_peak(inArray):
    """
    function that finds a peak in a list of unsorted integers.
    """
    if not inArray:
        return None
    newArray = []
    lenArray = len(inArray)

    for i in range(1, lenArray-1):
        newArray.append(inArray[i])
    searchPeak = newArray[0]
    for j in range(len(newArray)):
        if newArray[j] >= searchPeak:
            searchPeak = newArray[j]
    return searchPeak
