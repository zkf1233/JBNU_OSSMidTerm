# Program make a simple calculator

from distutils.log import error
import oper as op
import os

path = os.path.dirname(os.path.abspath(__file__))

print(path)

# calcLogf = 정상, errorLogf = 비정상
calcLogf=open(path+"/calc.log", "a")
errorLogf=open(path+"/error.log", "a")

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
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            sum = op.add(num1, num2)
            print(num1, "+", num2, "=", sum)
            calcLogf.write("%d\n" % sum)

        elif choice == '2':
            sub = op.sub(num1, num2)
            print(num1, "-", num2, "=", sub)
            calcLogf.write("%d\n" % sub)

        elif choice == '3':
            mul = op.multiply(num1, num2)
            print(num1, "*", num2, "=", mul)
            calcLogf.write("%d\n" % mul)
            
        elif choice =='4':
            div = op.divide(num1, num2)
            if(div == "er"):
                print("zde")
                errorLogf.write("zde\n")
            else:
                print(num1, "/", num2, "=", op.divide(num1,num2))
                calcLogf.write("%d\n" % div)
            

        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
            break

    else:
        print("Invalid Input")

calcLogf.close()
errorLogf.close()