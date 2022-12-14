from decimal import *
import sys
import logging as log

OPER_CODE = {
    '1' : "+",
    '2' : "-",
    '3' : "*",
    '4' : "/"
}

# Print operation result
def operationString(num1, num2, res, operator):
    return str("%s %s %s = %s" % (num1, operator, num2, res))

# This function adds two numbers
def add(x, y):
    try:
        value = Decimal(x) + Decimal(y)
        print(operationString(x, y, value, '+'))
        return float(value)
    except Exception as e:
        print(e, file=sys.stderr)
        return str('-1')

# This function subtracts two numbers
def subtract(x, y):
    try:
        value = Decimal(x) - Decimal(y)
        print(operationString(x, y, value, '-'))
        return float(value)
    except Exception as e:
        print(e, file=sys.stderr)
        return str('-1')

# This function multiplies two numbers
def multiply(x, y):
    try:
        value = Decimal(x) * Decimal(y)
        print(operationString(x, y, value, '*'))
        return float(value)
    except Exception as e:
        print(e, file=sys.stderr)
        return str('-1')

# This function divides two numbers
def divide (x, y):
    try:
        value = Decimal(x) / Decimal(y)
        print(operationString(x, y, value, '/'))
        return float(value)
    except DivisionByZero:
        print("ZeroDivisionError")
        return str('3')
    except Exception as e:
        print(e, file=sys.stderr)
        return str('-1')

# Function dictionary
OPERATION_DICT = {
    '1' : add, 
    '2' : subtract, 
    '3' : multiply, 
    '4' : divide
}

def operationFunc(operationCode, num1, num2):
    return OPERATION_DICT[operationCode](num1, num2)