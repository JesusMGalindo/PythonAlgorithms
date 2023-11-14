'''
Function will test a binary search tree and a red black tree by reading a file of numbers and inserting the number into both trees. It will then compare the heights and the number of nodes of each tree. If the file is "rand1000.txt" it will print the tree in decending order and rank.
Takes user input for a filename in the directory and inserts them onto a binary tree and red black tree and compares them.
'''

import os
import os.path
from bintrees import RBTree
 
global count
 
class Node(object):
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

    def insert(self, data):
        ''' For inserting the data in the Tree '''
        global count
        if self.data == data:
            count += 1
            return False        # As BST cannot contain duplicate data

        elif data < self.data:
            ''' Data less than the root data is placed to the left of the root '''
            if self.leftChild:
                return self.leftChild.insert(data)
            else:
                self.leftChild = Node(data)
                return True

        else:
            ''' Data greater than the root data is placed to the right of the root '''
            if self.rightChild:
                return self.rightChild.insert(data)
            else:
                self.rightChild = Node(data)
                return True

    def minValueNode(self, node):
        current = node

        # loop down to find the leftmost leaf
        while(current.leftChild is not None):
            current = current.leftChild

        return current

    def maxValueNode(self, node):
        current = node

        # loop down to find the leftmost leaf
        while(current.rightChild is not None):
            current = current.rightChild

        return current


    def delete(self, data,root):
        ''' For deleting the node '''
        if self is None:
            return None

        # if current node's data is less than that of root node, then only search in left subtree else right subtree
        if data < self.data:
            self.leftChild = self.leftChild.delete(data,root)
        elif data > self.data:
            self.rightChild = self.rightChild.delete(data,root)
        else:
            # deleting node with one child
            if self.leftChild is None:

                if self == root:
                    temp = self.minValueNode(self.rightChild)
                    self.data = temp.data
                    self.rightChild = self.rightChild.delete(temp.data,root) 

                temp = self.rightChild
                self = None
                return temp
            elif self.rightChild is None:

                if self == root:
                    temp = self.maxValueNode(self.leftChild)
                    self.data = temp.data
                    self.leftChild = self.leftChild.delete(temp.data,root) 

                temp = self.leftChild
                self = None
                return temp

            # deleting node with two children
            # first get the inorder successor
            temp = self.minValueNode(self.rightChild)
            self.data = temp.data
            self.rightChild = self.rightChild.delete(temp.data,root)

        return self

    def find(self, data):
        ''' This function checks whether the specified data is in tree or not '''
        if(data == self.data):
            return True
        elif(data < self.data):
            if self.leftChild:
                return self.leftChild.find(data)
            else:
                return False
        else:
            if self.rightChild:
                return self.rightChild.find(data)
            else:
                return False

    def preorder(self):
        '''For preorder traversal of the BST '''
        if self:
            print(str(self.data), end = ' ')
            if self.leftChild:
                self.leftChild.preorder()
            if self.rightChild:
                self.rightChild.preorder()

    def inorder(self):
        ''' For Inorder traversal of the BST '''
        if self:
            if self.leftChild:
                self.leftChild.inorder()
            print(str(self.data), end = ' ')
            if self.rightChild:
                self.rightChild.inorder()
                
    def inorderDec(self):
        ''' For Inorder traversal of the BST '''
        global count
        if self:
            if self.rightChild:
                yield from self.rightChild.inorderDec()
            yield count, self.data
            count -= 1
            if self.leftChild:
                yield from self.leftChild.inorderDec()

    def postorder(self):
        ''' For postorder traversal of the BST '''
        if self:
            if self.leftChild:
                self.leftChild.postorder()
            if self.rightChild:
                self.rightChild.postorder()
            print(str(self.data), end = ' ')

class Tree(object):
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root:
            return self.root.insert(data)
        else:
            self.root = Node(data)
            return True

    def delete(self, data):
        if self.root is not None:
            return self.root.delete(data,self.root)

    def find(self, data):
        if self.root:
            return self.root.find(data)
        else:
            return False

    def preorder(self):
        if self.root is not None:
            print()
            print('Preorder: ')
            self.root.preorder()

    def inorder(self):
        print()
        if self.root is not None:
            print('Inorder: ')
            self.root.inorder()
            
    def inorderDec(self):
        print()
        if self.root is not None:
            print('Inorder Decending: ')
            yield from self.root.inorderDec()

    def postorder(self):
        print()
        if self.root is not None:
            print('Postorder: ')
            self.root.postorder()
    
    def height(self, root): 
        # Check if the binary tree is empty
        if root is None:
            # If TRUE return 0
            return 0 
        # Recursively call height of each node
        leftAns = self.height(root.leftChild)
        rightAns = self.height(root.rightChild)
    
        # Return max(leftHeight, rightHeight) at each iteration
        return max(leftAns, rightAns) + 1
    
    def count_nodes(self, node):
        if node is None:
            return 0
        return 1 + self.count_nodes(node.leftChild) + self.count_nodes(node.rightChild)

def getHeight(root): 
        # Check if the binary tree is empty
        if root is None:
            # If TRUE return 0
            return 0 
        # Recursively call height of each node
        leftAns = getHeight(root.left)
        rightAns = getHeight(root.right)
    
        # Return max(leftHeight, rightHeight) at each iteration
        return max(leftAns, rightAns) + 1

bst = Tree()        # initialize trees
rb = RBTree()
count = 0

print("\nSelect a file to fill the tree.\nFiles in directory: " + str(os.listdir()))   # show file directory
filename = input("Enter file a file name: ")        # check if file exists
if not (os.path.exists(filename)):
    print("File not in directory. Exiting...") 
    exit()

text = open(filename, "r")                       # open file and append numbers into arrays
for line in text:                                # Loop through each line of the file
    line = line.split()
    for num in line:                             # Iterate over each number in line
        rb.insert(int(num), 0)          # insert number into binary tree and red black tree
        bst.insert(int(num))
text.close()

print("BSTree height:", bst.height(bst.root))       # display BST height
print("BSTree Node count:", bst.count_nodes(bst.root))  # display BST total nodes
print("BSTree Duplicates", count)
print("RBTree height:", getHeight(rb._root))        # display red black tree height
print("RBTree Node count:", rb.count)               # display red black tree total nodes
count = bst.count_nodes(bst.root) 

if filename == "rand1000.txt":                  # call in order desending generator and iterate until we get all keys and rank
    for rank, num in bst.inorderDec():
        print('[' + str(rank) + ']' + str(num), end = ', ')

