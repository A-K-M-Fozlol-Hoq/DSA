'''
Algorithm
step 1: Start
setp 2: Declare 3 variables named num1, num2 and sum
step 3: Read values of num1 and num2 from user
step 4: Add num1 and num2 and assign to sum variable (sum = num1 + num2)
setp 5: Show output
step 6: Stop
'''
print("this code will add two numbers and print result")
num1, num2, sum = None, None, None
try:
    num1 = int(input("Please enter first number: "))
    num2 = int(input("Please enter second number:"))
except ValueError:
    print("Invalid input. Please enter only integers.")
    exit()

sum = num1+ num2
print(f"sum of {num1} and {num2} is {sum}")