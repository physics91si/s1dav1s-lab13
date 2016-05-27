#!/usr/bin/python

# Lab 13
# Physics 91SI
# Spring 2016

import sys

def main():
    """Join command-line arguments and pass them to unitcalc(), then print."""
    calculation = ''.join(sys.argv[1:])
    print calc(calculation)

def calc(s):
    """Parse a string describing an operation on quantities with units."""

    # TODO make this robust for differently formatted inputs
    operators = findOperators(s)
    numbers = findNumbers(s)
    num1 = numbers[0]
    num2 = numbers[1]
    operation = operators[0]

    if operation=='+':
        return int(num1)+int(num2)
    elif operation=='-':
        return int(num1)-int(num2)
    elif operation=='*':
        return int(num1)*int(num2)
    elif operation=='/':
        return int(num1)/int(num2)

def findNumbers(s):
    numbers = []
    for j in findOperators(s):
        s.split(j)
    for k in s:
        if (type(k)==float):
            numbers.append(k)
    return numbers

def findOperators(s):
    operators = []
    for i in s:
        if (type(i)!=float):
            operators.append(i)
    return operators
    
        
        

if __name__ == "__main__": main()
