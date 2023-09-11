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
    def insert_head(self, new_node):
        temp_node = self.head
        self.head = new_node
        self.head.next = temp_node
        del temp_node
    def list_length(self):
        current_node = self.head
        length = 0
        while current_node is not None:
            length += 1
            current_node = current_node.next
        return length
    
    def insert_at(self, new_node, position):
        if position>self.list_length() or position<0:
            print("Invalid position")
            return
        if position is 0:
            self.insert_head(new_node)
        current_node = self.head
        current_node_position = 0
        while True:
            if position == current_node_position:
                previous_node.next = new_node
                new_node.next = current_node
                break
            previous_node = current_node
            current_node = current_node.next
            current_node_position += 1
    def delet_end(self):
        last_node = self.head
        while last_node.next is not None:
            previous_node= last_node
            last_node = last_node.next
        previous_node.next = None
            



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
print('\n',l_list.list_length(),' this is the current length of the linked list')
fourth_node = Node('start')
l_list.insert_head(fourth_node)
print("printing after inserthead")
l_list.print_list()
print('\n',l_list.list_length(),' this is the current length of the linked list')
fifth_node= Node("added")
l_list.insert_at(fifth_node, 2)
l_list.print_list()
l_list.delet_end()
print("after delete end")
l_list.print_list()