try:
    print("SIMPLE CALCULATOR :)")
    print("choose operator(+.-,*,/)")
    opr=input()
except ValueError:
    print("Please enter a valid operator shown above!.")
if(opr=="+"):
    try:
        first=int(input("ADD NUMBER: "))
        second=int(input("TO NUMBER: "))
        addition=int(first)+int(second)
        print(first,"+",second,"=",addition)
    except ValueError:
        print("Enter a valid input")
elif(opr=="-"):
    try:
        first=int(input("SUBTRACT NUMBER: "))
        second=int(input("FROM NUMBER: "))
        subraction=int(second)-int(first)
        print(second,"-",first,"=",subraction)
    except ValueError:
        print("Enter a valid input")
elif(opr=="*"):
    try:
        first=int(input("MULTIPLY NUMBER: "))
        second=int(input("TO NUMBER: "))
        multiplication=int(first)*int(second)
        print(first,"*",second,"=",multiplication)
    except ValueError:
        print("Enter a valid input")
elif(opr=="/"):
    try:
        first=int(input("DIVIDE NUMBER: "))
        second=int(input("BY NUMBER: "))
        division=int(first)/int(second)
        print(first,"/",second,"=",division)
    except ZeroDivisionError:
        print("Ooops! A number can't be divided by zero.")

