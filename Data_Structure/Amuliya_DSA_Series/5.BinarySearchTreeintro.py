#Here we learn about Binary Search Tree
#BST is a binary tree in which the value of each node is greater than or equal to any value stored in the left sub-tree, and less than or equal to any value stored in the right sub-tree.
#BST = Binary Search Tree

#here we initialize the class BST
class BST:
    def __init__(self,key):
        self.key = key
        self.lchild = None
        self.rchild = None
    
    def insert(self,data):
        if self.key is None:
            #that means the tree is empty
            self.key = data
            return#end of the function
        
        if self.key == data:
            return #ignore the duplicate values
        
        if self.key > data:
            #that means self.lchild is present
            if self.lchild:
                self.lchild.insert(data) #recursive call
            else:
                self.lchild = BST(data)#creating a new object/node
        else:
            if self.rchild:
                self.rchild.insert(data) #recursive call
            else:
                self.rchild = BST(data)#creating a new object/node
    
    #seraching node in the BST
    def search(self,data):
        if self.key == data:
            print("Node is Found")
            return
        
        if self.key > data:
            if self.lchild:
                self.lchild.search(data)
            else:
                print("Node is not present in the tree")
        
        if self.key < data:
            if self.rchild:
                self.rchild.search(data)
            else:
                print("Node is not present in the tree")
    
    #BST Preorder Travarsal
    def preorder(self):
        print(self.key,end=" ")#printing the result at same line
        if self.lchild:
            self.lchild.preorder()
        if self.rchild:
            self.rchild.preorder()
    
    #BST Preorder Travarsal
    def inorder(self):
        if self.lchild:
            self.lchild.inorder()
        print(self.key,end=" ")#printing the result at same line
        if self.rchild:
            self.rchild.inorder()
    
    #BST Postorder Travarsal
    def postorder(self):
        if self.lchild:
            self.lchild.postorder()
        if self.rchild:
            self.rchild.postorder()
        print(self.key,end=" ")#printing the result at same line
        
    
     
        
        
        
    
#creating a object of BST class
root = BST(10)
list1 = [20,4,30,1,5,6]
for i in list1:
    root.insert(i)
#root.search(50)
print("Preorder Travarsal of BST is: ")
root.preorder()
print("\nInorder Travarsal of BST is: ")
root.inorder()
print("\nPostorder Travarsal of BST is: ")
root.postorder()