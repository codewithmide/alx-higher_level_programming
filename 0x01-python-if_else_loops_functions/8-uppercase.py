#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) > 96 and ord(i) < 123:
            i = chr(ord(i) - 32)
        print("{}".format(i), end="")
    print()
