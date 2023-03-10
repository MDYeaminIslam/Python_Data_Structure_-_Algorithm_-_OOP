#Linked List is also a linear data structure but it is not stored in a contiguous memory location.
#Simply Linked List
#implementing a singly linked List using class

class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None #Null == None.

class LinkedList:
    def __init__(self):
        self.head = None #creating empty LinkedList
    
    #travers a Linked List
    #printing all the elements of linked list.
    def print_LL(self):
        if self.head is None:
            print("Linked List is empty!")
        else:
            n = self.head
            while n is not None:
                print(n.data,"--->",end=" ")
                n = n.ref
    
    #adding a node when linked List totally empty
    #that means adding a node if there is no node exits in the Linked List
    
    def insert_empty(self,data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
            
        else:
            print("Linked List is Not Empty!")
    
    
    def add_begin(self,data):
        #creating object of Node class
        new_node = Node(data) #creating object with the help of Node class
        new_node.ref = self.head
        self.head = new_node #storing new_node ref value in head and new_node become first Node

    
    def add_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref  
            n.ref = new_node
            
        
    #we will add a node after a particular node in the linked list
    #X is the node before which we want to add a new node
    def add_after(self,data,X):
        n = self.head
        while n is not None:
            if X == n.data:
                break
            n = n.ref
        if n is None:
            print("Node is not present in the Linked List")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node
        
    #we will add a node before a particular node in the Linked List
    #X is the node before which we want to add a new node
    def add_before(self,data,X):
        if self.head is None:
            print("Linked List is empty!")
            return
        #if we want to add a node before the first node
        if self.head.data == X:
            #creating object of Node class
            new_node = Node(data) #creating object with the help of Node class
            new_node.ref = self.head
            self.head = new_node #storing new_node ref value in head and new_node become first Node 
            return
        #now we are going to add a node before a node other than the first node.
        n = self.head
        while n is not None:
            if n.ref.data == X:
                break
            n = n.ref
        if n.ref is None:
            print("Node is not found")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node
                
            
LL1 = LinkedList()
"""
LL1.add_begin(299)
LL1.add_end(4000)
LL1.add_after(5678,299) #inserting 5678 after 299 in the Linked List
LL1.add_before(443,4000)
"""
LL1.insert_empty(200)

LL1.print_LL()