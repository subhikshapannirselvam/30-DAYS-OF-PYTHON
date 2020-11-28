import math
print("Python calculator")
print("1.Addition\n2.Subraction\n3.Multiplication\n4.Division\n5.Raising power\n6.square root\n7.log\n8.exponent")
opr=int(input("What operations would you like to perform?"))
if opr==1:
    a=int(input("Enter first number:"))
    b=int(input("Enter second number:"))
    print("The answer is ",a+b)
elif opr==2:
    a=int(input("Enter first number:"))
    b=int(input("Enter second number:"))
    print("The answer is ",a-b)
elif opr==3:
    a=int(input("Enter first number:"))
    b=int(input("Enter second number:"))
    print("The answer is ",a*b)
elif opr==4:
    a=int(input("Enter first number:"))
    b=int(input("Enter second number:"))
    print("The answer is ",a/b)
elif opr==5:
    a=int(input("Enter first number:"))
    b=int(input("Enter second number:"))
    print("The answer is ",math.pow(a,b))
elif opr==6:
    a=int(input("Enter the number:"))
    print("The answer is ",math.sqrt(a))
elif opr==7:
    a=int(input("Enter the number:"))
    print("The answer is ",math.log(a))
elif opr==8:
    a=int(input("Enter the number:"))
    print("The answer is ",math.exp(a))
