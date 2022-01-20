
def calculator():
    num1=int(input("your first number:"))
    operator=input("operator type:")
    num2=int(input("your second number:"))

    if operator=="+":
        print(num1+num2)
        calculator()
    elif operator=="-":
        print(num1-num2)
        calculator()
    elif operator=="*":
        print(num1*num2)
        calculator()
    elif operator=="/":
        print(num1/num2)
        calculator()
    
calculator()