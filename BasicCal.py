num1 = int(input("Enter first no : "))
num2 = int(input("Enter second no : "))
operation = input("Enter operation you want to perform:\n+ for additon\n- for subtraction\n* for Multiplication \n/ for divide. ")
if operation=="+":
    print("Addition",num1+num2)
elif operation=="-":
    print("Subtraction",num1-num2)
elif operation=="*":
    print("Multiplication",num1*num2)
elif operation=="/":
    print("Division",num1/num2)
elif b == 0 :
    print("Division with zero is not possible.Enter another no in place of zero in b.")
else:
    print("Enter a valid operation from the above options.")