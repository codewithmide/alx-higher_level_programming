#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    argv = sys.argv
    op = argv[2]
    num1 = argv[1]
    num2 = argv[3]
    result = 0
    if len(sys.argv) != 4:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)

    if op == "+":
        print('{:d} + {:d} = {:d}'.format(a, b, add(a, b)))
    elif op == "-":
        print('{:d} - {:d} = {:d}'.format(a, b, sub(a, b)))
    elif op == "*":
        print('{:d} * {:d} = {:d}'.format(a, b, mul(a, b)))
    elif op == "/":
        print('{:d} / {:d} = {:d}'.format(a, b, div(a, b)))
    else:
        print('Unknown operator. Available operators: +, -, * and /')
