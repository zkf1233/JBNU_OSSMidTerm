from decimal import *
import sys
import logging as log

# Print operation result
def operationString(num1, num2, res, operator):
    return "%s %s %s = %s" % (num1, operator, num2, res)

# This function adds two numbers
def add(x, y):
    try:
        value = Decimal(x) + Decimal(y)
        print(operationString(x, y, value, '+'))
        return value
    except Exception as e:
        print(e, file=sys.stderr)

# This function subtracts two numbers
def subtract(x, y):
    try:
        value = Decimal(x) - Decimal(y)
        print(operationString(x, y, value, '-'))
        return value
    except Exception as e:
        print(e, file=sys.stderr)

# This function multiplies two numbers
def multiply(x, y):
    try:
        value = Decimal(x) * Decimal(y)
        print(operationString(x, y, value, '*'))
        return value
    except Exception as e:
        print(e, file=sys.stderr)

# This function divides two numbers
def divide (x, y):
    try:
        value = Decimal(x) / Decimal(y)
        print(operationString(x, y, value, '/'))
        return value
    except Exception as e:
        if(e == ZeroDivisionError):
            print("ZeroDivisionError")
        else:
            print(e, file=sys.stderr)

# Function dictionary
OPERATION_DICT = {
    '1' : add, 
    '2' : subtract, 
    '3' : multiply, 
    '4' : divide
}

def operationFunc(operationCode, num1, num2):
    OPERATION_DICT[operationCode](num1, num2)