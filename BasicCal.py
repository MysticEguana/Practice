a = int(input("Enter first no : "))
b = int(input("Enter second no : "))
operation = input("Enter operation you want to perform:\n+ for additon\n- for subtraction\n* for Multiplication \n/ for divide. ")
if operation=="+":
    print("Addition",a+b)
elif operation=="-":
    print("Subtraction",a-b)
elif operation=="*":
    print("Multiplication",a*b)
elif operation=="/":
    print("Division",a/b)
elif b == 0 :
    print("Division with zero is not possible.Enter another no in place of zero in b.")
else:
    print("Enter a valid operation from the above options.")