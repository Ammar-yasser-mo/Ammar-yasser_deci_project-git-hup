print("calculator")
print("*********************************************************")

num1 = float(input("please enter first number: "))
operator = input("please enter the operator: ")
num2 = float(input("please enter second number: "))

if operator == "+":
    print(num1+num2)
elif operator == "-":
    print(num1-num2)
elif operator == "*":
    print(num1*num2)
elif operator == "/":
    print(num1/num2)
else:
    print("wrong operator ; please try again")