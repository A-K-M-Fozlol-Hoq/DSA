class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    def print(self):
        print(self.data, self.next)

class LinkedList:
    def __init__(self):
        self.head = None
    def insert(self,new_node):
        if(self.head==None):
            self.head = new_node
        else:
            last_node = self.head
            while(True):
                if(last_node.next == None):
                    break
                else:
                    last_node = last_node.next
            last_node.next = new_node
    def print_list(self):
        if self.head is None:
            print("Linked list is empty!")
        else:
            current_node = self.head
            while True:
                print(current_node.data, end=' ')
                if current_node.next is None:
                    break
                print('=>', end=' ')
                current_node = current_node.next



# Test my linked list
first_node = Node(2)
second_node = Node('ok')
third_node = Node('hey')
l_list = LinkedList()
l_list.insert(first_node)
l_list.insert(second_node)
l_list.insert(third_node)
print("this is your linked list: ")
l_list.print_list()