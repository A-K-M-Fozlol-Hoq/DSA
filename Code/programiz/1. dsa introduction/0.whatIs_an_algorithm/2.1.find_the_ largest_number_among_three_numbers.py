# This program takes three numbers and finds the largest one.

num1, num2, num3 = None, None, None

try:
    num1 = int(input("Please enter the first number: "))
    num2 = int(input("Please enter the second number: "))
    num3 = int(input("Please enter the third number: "))
except ValueError:
    print("Invalid input. Please enter only integers.")
    exit()

if num1 >= num2 and num1 >= num3:
    print(f"{num1} is the largest number.")
elif num2 >= num1 and num2 >= num3:
    print(f"{num2} is the largest number.")
else:
    print(f"{num3} is the largest number.")
