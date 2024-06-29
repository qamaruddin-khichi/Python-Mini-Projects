# Python Mini Projects

## Table of Contents

1. [BMI Calculator](#bmi-calculator)
    - [Code](#bmi-calculator-code)
2. [Simple Calculator](#simple-calculator)
    - [Code](#simple-calculator-code)

---

# BMI Calculator

## What is BMI?

Body Mass Index (BMI) measures body fat based on height and weight that applies to adult men and women. It is an easy and non-invasive method to assess whether a person has a healthy body weight. To learn more about BMI, refer to [this article](https://www.verywellfit.com/bmi-what-is-bmi-or-body-mass-index-3120088).

### BMI Calculator Code

```python
# BMI Calculator

Name = input("Enter your name : ")

Weight = int(input("Enter your weight in pounds : "))

Height = int(input("Enter your height in inches : "))

BMI = (Weight * 703) / (Height * Height)

print(f'{Name}, your BMI is : {BMI:.2f}')

if BMI < 18.5:
    print(f'{Name}, you are underweight and your health risks are minimal.')

elif BMI >= 18.5 and BMI < 24.99:
    print(f'{Name}, you have normal weight and your health risks are minimal.')

elif BMI >= 25 and BMI < 29.99:
    print(f'{Name}, you are overweight and your health risks are increased.')

elif BMI >= 30 and BMI < 34.99:
    print(f'{Name}, you have obesity and your health risks are high.')

elif BMI >= 35 and BMI < 39.99:
    print(f'{Name}, you have morbidly obesity and your health risks are extremely high.')

elif BMI >= 40:
    print(f'{Name}, you have severe obesity and your health risks are extremely high.')
else:
    print("Please enter valid inputs.")
```

---

# Simple calculator
This repository contains a simple Python script for basic arithmetic operations: addition, subtraction, multiplication, and division.

### Simple Calculator Code

```python
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
```
