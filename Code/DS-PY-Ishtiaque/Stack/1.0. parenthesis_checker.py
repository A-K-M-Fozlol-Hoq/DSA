from _Stack import Stack

def parentheseis_checker(str):
    stack = Stack()
    isValid = True
    for i in str:
        if(i =="("):
            stack.push("(")
        else:
            if (stack.isEmpty()):
                isValid=False
                break
            else:
                stack.pop()
    if(isValid and stack.isEmpty()):
        print("Valid")
    else:
        print("Invalid")

parentheseis_checker('(())')
parentheseis_checker('(()))')
parentheseis_checker('((())')
parentheseis_checker('())())')
parentheseis_checker('((())())')

