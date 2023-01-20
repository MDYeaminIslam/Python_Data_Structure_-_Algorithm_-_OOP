#Linked List is also a linear data structure but it is not stored in a contiguous memory location.
#Simply Linked List
#implementing a singly linked List using class

class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None

class LinkedList:
    def __init__(self):
        self.head = None #creating empty LinkedList
    
    #travers a Linked List
    def print_LL(self):
        if self.head is None:
            print("Linked List is empty!")
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.ref
    
    def add_begin(self,data):
        #creating object of Node class
        new_node = Node(data) #creating object with the help of Node class
        new_node.ref = self.head
        self.head = new_node #storing new_node ref value in head and new_node become first Node

LL1 = LinkedList()
LL1.add_begin(34)
LL1.add_begin(10)
LL1.print_LL()