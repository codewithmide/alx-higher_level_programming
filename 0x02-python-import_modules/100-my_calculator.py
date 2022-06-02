#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv, exit
    from calculator_1 import add, sub, mul, div
    length = len(argv)
if length != 4:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    exit(1)
if length == 4:
    op = argv[2]
    a = int(argv[1])
    b = int(argv[3])
    if op == "+":
        print('{:d} + {:d} = {:d}'.format(a, b, add(a, b)))
    elif op == "-":
        print('{:d} - {:d} = {:d}'.format(a, b, add(a, b)))
    elif op == "*":
        print('{:d} * {:d} = {:d}'.format(a, b, add(a, b)))
    elif op == "/":
        print('{:d} / {:d} = {:d)}'.format(a, b, add(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
    exit(1)
