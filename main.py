# Program make a simple calculator

import sys
import oper as op
import logging as log

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    # take input from the user
    choice = input("Enter choice(1/2/3/4): ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except Exception as e:
            print("Please enter a number :", e, file=sys.stderr)
            continue
        
        # Operation
        op.operationFunc(choice, str(num1), str(num2))
        
        # Check if user wants another calculation
        # Break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
            recheck = input("Are you sure? (yes/no): ")
            if (recheck == "yes"):
                break

    else:
        print("Invalid Input")