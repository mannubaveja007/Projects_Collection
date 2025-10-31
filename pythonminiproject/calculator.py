print("welcome to Calulator app")
def calculator():
    try:
        number1 = int(input("Enter the first number :- "))
        op = input("enter the operator (+,*,-,/)").strip()
        number2 = int(input("Enter the second number : - " ))
        if op == "+":
            result = number1+number2
        elif op == "-":
            result = number2-number1
        elif op == "*":
            result = number1*number2
        elif op == "/":
            if number2 == 0:
                print("you cant divide number by zero")
                return
            result == number2/number1
        else:
            print("Invalid Operator")
            return
        print(f"Result is {result}")
    except ValueError:
        print("Error: Please enter valid numbers.")
    

calculator()
