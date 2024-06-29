# BMI Calculator

Name = input("Enter your name : ")

Weight = int(input("Enter your weight in pounds : "))

Height = int(input("Enter your height in inches : "))

BMI = (Weight * 703) / (Height * Height)

print(f'{Name}, your BMI is : {BMI}')

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


# A better version of BMI Calculator

Name = input("Enter your name: ")

Weight = float(input("Enter your weight in pounds: "))
Height = float(input("Enter your height in inches: "))

BMI = (Weight * 703) / (Height * Height)

print(f'{Name}, your BMI is: {BMI:.2f}')

if BMI < 18.5:
    print(f'{Name}, you are underweight and your health risks are minimal.')
elif 18.5 <= BMI < 24.99:
    print(f'{Name}, you have a normal weight and your health risks are minimal.')
elif 25 <= BMI < 29.99:
    print(f'{Name}, you are overweight and your health risks are increased.')
elif 30 <= BMI < 34.99:
    print(f'{Name}, you have obesity and your health risks are high.')
elif 35 <= BMI < 39.99:
    print(f'{Name}, you have morbid obesity and your health risks are extremely high.')
elif BMI >= 40:
    print(f'{Name}, you have severe obesity and your health risks are extremely high.')
else:
    print("Please enter valid inputs.")
