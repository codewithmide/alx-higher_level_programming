#!/usr/bin/python3


def find_peak(list_of_integers):
    '''
        Finds the peak in a list of numbers
    '''
    arr = list_of_integers
    n = len(arr)
    if n == 0:
        return None
    mid = n // 2
    if (mid == n - 1 or arr[mid] >= arr[mid + 1]) and (mid == 0 or arr[mid] >=
                                                       arr[mid - 1]):
        return arr[mid]
    if mid != n - 1 and arr[mid + 1] > arr[mid]:
        return find_peak(arr[mid + 1:])
    return find_peak(arr[:mid])
