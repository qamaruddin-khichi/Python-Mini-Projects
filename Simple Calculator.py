# Simple calculator

num1 = float(input("Enter num1 :"))

sign = input("Enter the sign :")

num2 = float(input("Enter num2 :"))


if sign == "+":
    print(num1 + num2)
elif sign == "-":
    print(num1 - num2)
elif sign == "*":
    print(num1 * num2)
elif sign == "/":
    if num2 != 0:
        print(num1 / num2)        
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid sign")