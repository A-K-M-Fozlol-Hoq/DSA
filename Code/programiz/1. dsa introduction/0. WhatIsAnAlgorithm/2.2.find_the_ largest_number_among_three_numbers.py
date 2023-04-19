# This program takes three numbers and finds the largest one.

try:
    num1 = int(input("Please enter the first number: "))
    num2 = int(input("Please enter the second number: "))
    num3 = int(input("Please enter the third number: "))
except ValueError:
    print("Invalid input. Please enter only integers.")
    exit()

largest_num = max(num1, num2, num3)
print(f"The largest number is: {largest_num}")
