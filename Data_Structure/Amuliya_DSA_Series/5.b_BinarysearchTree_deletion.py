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

    #deletion of node in BST
    def delete(self,data,current):
        if self.key is None:
            print("Tree is empty")
            return
        if data < self.key:
            if self.lchild:
                self.lchild = self.lchild.delete(data,current)
            else:
                print("Given Node is not present in the tree")
        elif data > self.key:
            if self.rchild:
                self.rchild = self.rchild.delete(data,current)
            else:
                print("Given Node is not present in the tree")
        else:
            #deleting a node with no child/one child
            if self.lchild is None:
                temp = self.rchild
                if data == current:
                    self.key = temp.key
                    self.lchild = temp.lchild
                    self.rchild = temp.rchild
                    temp = None
                    return
                self = None
                return temp
            
            if self.rchild is None:
                temp = self.lchild
                if data == current:
                    self.key = temp.key
                    self.lchild = temp.lchild
                    self.rchild = temp.rchild
                    temp = None
                    return
                self = None
                return temp
            #we want to find smallest node in right subtree and thats why we use node variable
            #deleting a node with two child
            node = self.rchild
            while node.lchild:
                node = node.lchild
            #storing smallest right subtree value in the root node
            self.key = node.key
            self.key = self.rchild.delete(node.key,current)
        return self
    
    #finding the minimum value/node of the tree
    def min_node(self):
        current_node = self
        #here current_node is the root node
        #this loop will run until the left child is present
        while current_node.lchild:
            current_node = current_node.lchild
        print("\nMinimum value of the tree is: ",current_node.key)
    
    
    #finding the maximum value/node of the tree
    def max_node(self):
        current_node = self
        #here current_node is the root node
        #this loop will run until the right child is present
        while current_node.rchild:
            current_node = current_node.rchild
        print("\nMaximum value of the tree is: ",current_node.key)
    
        

def count(node):
    if node is None:
        return 0
    return 1 + count(node.lchild) + count(node.rchild)      
    
#creating a object of BST class
root = BST(10)
list1 = [2,13,7,34,99]
for i in list1:
    root.insert(i)
#root.search(50)
'''
print("Preorder Travarsal of BST is: ")
root.preorder()
print("\nInorder Travarsal of BST is: ")
root.inorder()
print("\nPostorder Travarsal of BST is: ")
root.postorder()


'''
print("Preorder Travarsal of BST is: ")
root.preorder()

'''
#this one if for deleting the root node
if count(root)>1:
    root.delete(10,root.key)
else:
    print("Can't perform deletion operation")
    

print("\nPreorder Travarsal of BST is: ")
print("\nAfter deleting :")
root.preorder()

'''


#print(count(root))

root.max_node()
root.min_node()
