class Node:
    """Represents a node in a linked list"""
    def __init__(self, item):
        self.data= item
        self.next =None
    def __str__(self):
        return str(self.data)

class LinkedList:
    """Represents a single linked list data structure"""
    def __init__(self):
        self.head=None
    def add(self, new_item):
        """creates a new node with 'new_item' and adds it at front"""
        node = Node(new_item)
        node.next = self.head
        self.head = node
        return self.head
    def __str__(self):
        """Returns a string that represents all the nodes from head in a list"""
        output=[]
        curr = self.head
        while curr:
            output.append(curr.data)
            curr= curr.next
        return  str(output)
    def delete(self, item):
        """Delete an item from the linke list if exists"""
        # Case 0: Delete first node
        if self.head.next == item:
            self.head= self.head.next
            return  self.head
        # Case 1: Delete a middle node
        prev=None
        curr= self.head
        while curr and curr.data != item:
            prev= curr
            curr= curr.next
        if curr:
            prev.next = curr.next
        return self.head
        # Case 3: Item doesn't exist

llist = LinkedList()
llist.add(2)
llist.add(4)
llist.add(6)
print(llist)
print(llist.delete(4))
print(llist)