# Program make a simple calculator

import sys
import oper as op
import logging as log

logFileManager = log.logManager()

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
            logFileManager.errorLogWrite('1', e.args[0])
            continue
        
        # Operation
        result = op.operationFunc(choice, str(num1), str(num2))
        
        # Check if user wants another calculation
        # Break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")

        while next_calculation.lower() != "yes" and next_calculation.lower() != "no":
            print("Please answer yes or no")
            next_calculation = input("Let's do next calculation? (yes/no): ")

        if next_calculation.lower() == "no":
            recheck = input("Are you sure? (yes/no): ")
            if (recheck.lower() == "yes"):
                break
        elif next_calculation.lower == "yes":
            continue

    else:
        logFileManager.errorLogWrite('2', )
        print("Invalid Input")