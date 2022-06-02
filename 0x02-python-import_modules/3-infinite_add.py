#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    argc = len(argv)
    result = 0
    for i in range(1, argc):
        result += int(argv[i])
    print(f'{result:d}')
