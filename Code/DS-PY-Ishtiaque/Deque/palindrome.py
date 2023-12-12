from deque import Deque

string = input("please enter your string:")
is_palindrome = True
queue = Deque()
for st in string:
    queue.addFront(st)
while queue.size()>1:
    front = queue.removeFront()
    reer = queue.removeRear()
    if front != reer:
        is_palindrome = False
        
if is_palindrome:
    print("Entered string is palindrome")
else:
    print("Entered string is not palindrome")