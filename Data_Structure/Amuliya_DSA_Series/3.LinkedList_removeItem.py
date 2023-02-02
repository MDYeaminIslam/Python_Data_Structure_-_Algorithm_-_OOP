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
    
    #deleting the first node from the Linked List
    def delete_begin(self):
        if self.head is None:
            print("Linked List is empty and you can't delete any node!")
        else:
            self.head = self.head.ref
    
    #deleting the last node from the Linked List
    def delete_end(self):
        if self.head is None:
            print("Linked List is empty and you can't delete any node!")
        #when Linked List contains only one node than delete this way
        elif self.head.ref is  None:
            self.head = None
        #when Linked List contains more than one node than delete this way
        else:
            n = self.head
            while n.ref.ref is not None:
                n = n.ref
            n.ref = None
    #deleting a node by value/deleting selected value from the Linked List that user given
    def delete_by_value(self,X):
        if self.head is None:
            print("Can't delete any node because Linked List is empty!")
            return #if we don't want else part of this "if" statement than we can give "return"
        if X==self.head.data:
            self.head = self.head.ref
            
        n = self.head
        while n.ref is not None:
            if X==n.ref.data:
                break
            n = n.ref
            
        if n.ref is None:
            print("Node is not present in the Linked List")
        else:
            n.ref = n.ref.ref
            
            
LL1 = LinkedList()
LL1.add_begin(20)
LL1.add_begin(40)
LL1.add_begin(60)
LL1.add_begin(80)
LL1.add_begin(90)
#LL1.delete_begin() #deleting the first node from the Linked List
#LL1.delete_end() #deleting the last node from the Linked List
LL1.delete_by_value(60)
LL1.print_LL()