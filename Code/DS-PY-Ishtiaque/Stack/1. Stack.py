class Stack:
    '''Stack data structure'''
    def __init__(self):
        self.items=[]
    def push(self,item):
        self.items.append(item)
    def pop(self):
        if(self.items != []):
            return self.items.pop()
        else:
            print("No items to pop")
    def peek(self):
        return self.items[-1]
    def isEmpty(self):
        return len(self.items)==0
    def size(self):
        return len(self.items)
    def __str__(self):
        return ' '.join(map(str, self.items))

stack =Stack()
print(stack)
stack.push(1)
stack.push(2)
print(stack)
print(stack.isEmpty(),'isempty')
print(stack.peek())
print(stack.size(),'size')
stack.pop()
print(stack.pop())
print(stack.isEmpty(),'isempty')
print(stack.pop(),'pop while stack is []')