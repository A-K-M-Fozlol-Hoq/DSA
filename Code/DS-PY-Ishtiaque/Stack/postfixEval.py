from _Stack import Stack

def postfixEval(string):
    stack = Stack()
    for item in string:
        if item in '0123456789+-*/':
            if item in ["+","-","*","/"]:
                num1= int(stack.pop())
                num2= int(stack.pop())
                result = domath(item, num1, num2)
                stack.push(result)
            else:
                stack.push(item)
    return stack.pop()

def domath(operator,num1,num2):
    if(operator == '+'):
        return num2+num1
    elif(operator == '-'):
        return num2-num1
    elif (operator == '*'):
        return num2*num1
    else:
        return (num2/num1)

print(postfixEval('23+45+*'))
print(postfixEval('23+4+'))
print(postfixEval('34*25*+'))
print(postfixEval('34*2 j 5*+ df'))