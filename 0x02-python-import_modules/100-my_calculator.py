#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv, exit
    from calculator_1 import add, sub, mul, div
if len(argv) != 4:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    exit(1)
a = int(argv[1])
b = int(argv[3])
if argv[2] == "+":
    print('{:d} + {:d} = {:d}'.format(a, b, add(a, b)))
elif argv[2] == "-":
    print('{:d} - {:d} = {:d}'.format(a, b, add(a, b)))
elif argv[2] == "*":
    print('{:d} * {:d} = {:d}'.format(a, b, add(a, b)))
elif argv[2] == "/":
    print('{:d} / {:d} = {:d)}'.format(a, b, add(a, b)))
else:
    print("Unknown operator. Available operators: +, -, * and /")
    exit(1)
