#Here we learn about Binary Search Tree
#BST is a binary tree in which the value of each node is greater than or equal to any value stored in the left sub-tree, and less than or equal to any value stored in the right sub-tree.
#BST = Binary Search Tree

#here we initialize the class BST
class BST:
    def __init__(self,key):
        self.key = key
        self.lchild = None
        self.rchild = None
    
#creating a object of BST class
root = BST(10)
print(root.key)
print(root.lchild)
print(root.rchild)