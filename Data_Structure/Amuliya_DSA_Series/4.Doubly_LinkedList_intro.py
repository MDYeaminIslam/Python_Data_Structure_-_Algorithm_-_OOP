#Doubly Linked List
class Node:
    def __init__(self,data):
        self.data = data
        self.nref = None #Null == None.
        self.pref = None

class doublyLL:
    def __init__(self):
        self.head = None
        
    #travers a Linked List
    #printing all the elements of linked list.
    def print_LL_forward(self):
        if self.head is None:
            print("Linked List is empty!")
        else:
            n = self.head
            while n is not None:
                print(n.data,"--->",end=" ")
                n = n.nref
    
    #travers a Linked List
    #printing all the elements of linked list.
    def print_LL_reverse(self):
        print()
        if self.head is None:
            print("Linked List is empty!")
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            while n is not None:
                 print(n.data,"--->",end=" ")
                 n = n.pref
    #creating a node when doubly linked list is empty()
    def insert_empty(self,data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
            
        else:
            print("Doubly Linked List is not empty!")
    
    def add_begin(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.nref = self.head
            self.head.pref = new_node
            self.head = new_node
            
    def add_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            n.nref = new_node
            new_node.pref = n
            
    #adding element after seletecd node
    def add_after(self,data,x):
        if self.head is None:
            print("Doubly Linked List is empty!")
        else:
            n = self.head
            while n is not None:
                if x == n.data:
                    break
                n = n.nref
            if n is None:
                print("Given Node is not present is Doubly Linked List")
                
            else:
                new_node = Node(data)
                new_node.nref = n.nref
                new_node.pref = n
                if n.nref is not None:
                    n.nref.pref = new_node
                n.nref = new_node
    #adding element before selected node
    def add_before(self,data,x):
        if self.head is None:
            print("Doubly Linked List is empty!")
        else:
            n = self.head
            while n is not None:
                if x == n.data:
                    break
                n = n.nref
            if n is None:
                print("Given Node is not present is Doubly Linked List")
            else:
                new_node = Node(data)
                new_node.nref = n
                new_node.pref = n.pref
                if n.pref is not None:
                    n.pref.nref = new_node
                else:
                    self.head = new_node
                n.pref = new_node #this one is for first node.
    #deleting a node
    def delete_begin(self):
        if self.head is None:
            print("Doubly Linked List is empty can't delete node!")
            return
        #deleting single node from the doubly linked list
        if self.head.nref is None:
            self.head = None
            print("Doubly Linked List is empty!")
        #if there are more than one node is the doubly linked list
        else:
            self.head = self.head.nref
            self.head.pref = None
            
    def delete_end(self):
        if self.head is None:
            print("Doubly Linked List is empty can't delete node!")
            return
        
        if self.head.nref is None:
            self.head = None
            print("Doubly Linked List is empty after deleting the node!")
            
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            n.pref.nref = None
    
    def delete_by_value(self,x):
        if self.head is None:
            print("Doubly Linked List is empty can't delete node!")
            return
        #deleting only one node from the doubly linked list
        if self.head.nref is None:
            if x==self.head.data:
                self.head = None
            else:
                print("Node is not present in the Doubly Linked List!")
            return
        #deleting first node
        if self.head.data == x:
            self.head = self.head.nref
            self.head.pref = None
            return
        #deleting middle node
        n = self.head
        while n.nref is not None:
            if x==n.data:
                break
            n = n.nref
        if n.nref is not None:
            n.nref.pref = n.pref
            n.pref.nref = n.nref
        else:
            if n.data == x:
                n.pref.nref = None
            else:
                print("Node is not present in the Doubly Linked List!")
        


ddl = doublyLL()
#ddl.insert_empty(200)
ddl.add_begin(4)
#ddl.add_after(10,4)
ddl.add_before(10,4)
ddl.add_end(20)
#ddl.delete_begin()
#ddl.delete_end()
ddl.delete_by_value(4)
ddl.print_LL_forward()

#ddl.print_LL_reverse()