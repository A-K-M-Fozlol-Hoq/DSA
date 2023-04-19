'''
Algorithm-
Step 1: Start
Step 2: Declare variables a,b and c.
Step 3: Read variables a,b and c.
Step 4: If a > b
           If a > c
              Display a is the largest number.
           Else
              Display c is the largest number.
        Else
           If b > c
              Display b is the largest number.
           Else
              Display c is the greatest number.  
Step 5: Stop
'''
print("This code will take 3 numbers and find the larger number.")
a,b,c = None, None, None
try:
    a = int(input("Please enter first number: "))
    b = int(input("Please enter second number: "))
    c = int(input("Please enter third number: "))
except ValueError:
    print("Invalid input. Please enter only integers.")
    exit()
    
if(a>b):
    if(a>c):
        print(f"a= {a} is the larger number.")
    else:
        print(f"c= {c} is the larger number.")
else:
    if(b>c):
        print(f"b= {b} is the larger number.")
    else:
        print(f"c= {c} is the largest number")