from stack import Stack
print('infixToPostfix')
def infixToPostfix(string):
    stack = Stack()
    output=[]
    power ={}
    power['(']= 1
    power['-']= 2
    power['+']= 3
    power['/']= 4
    power['*']= 5
    for item in string:
        if item in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ()+-*/':
            if item in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                output.append(item)
            elif item=='(':
                stack.push(item)
            elif item ==')':
                while(stack.peek() != '('):
                    output.append(stack.pop())
            else:
                while(not stack.isEmpty() and power[stack.peek()]>= power[item]):
                    output.append(stack.pop())
                stack.push(item)
    while(not stack.isEmpty()):
        output.append(stack.pop())
    return " ".join(output)

print(infixToPostfix("A * B + C * D")) #A B * C D * +
print(infixToPostfix("( A + B ) * C - ( D - E ) * ( F + G )")) #A B + C * D E - F G + * -

