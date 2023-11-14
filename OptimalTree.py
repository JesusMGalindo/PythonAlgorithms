mport json
import matplotlib.pyplot as plot
from operator import itemgetter
import random
import requests
from wordcloud import WordCloud

track = 1
count = 0

class Node(object):
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

    def insert(self, data):
        ''' For inserting the data in the Tree '''
        if self.data == data:
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

    def outorder(self):
        ''' For decending Inorder traversal of the BST '''
        global count
        if self:
            if self.rightChild:
               yield from self.rightChild.outorder()
            yield count, self.data
            count -= 1
            if self.leftChild:
               yield from self.leftChild.outorder()

    def postorder(self):
        ''' For postorder traversal of the BST '''
        if self:
            if self.leftChild:
                self.leftChild.postorder()
            if self.rightChild:
                self.rightChild.postorder()
            print(str(self.data), end = ' ')

class BST(object):
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

    def outorder(self):
        print()
        if self.root is not None:
            print('Outorder: ')
            yield from self.root.outorder()

    def postorder(self):
        print()
        if self.root is not None:
            print('Postorder: ')
            self.root.postorder()


    def getHeight(self,root):
     
        # Check if the binary tree is empty
        if root is None:
            # If TRUE return 0
            return 0 
        # Recursively call height of each node
        leftAns = self.getHeight(root.leftChild)
        rightAns = self.getHeight(root.rightChild)
     
        # Return max(leftHeight, rightHeight) at each iteration
        return max(leftAns, rightAns) + 1

    def countNodes(self,node):
        if node is None:
            return 0
        return 1 + self.countNodes(node.leftChild) + self.countNodes(node.rightChild)

#https://www.datacareer.de/blog/accessing-the-news-api-in-python/
def API(): 
    key = "ebb00ca321b64ea8826998baf9213a49"
    url = 'https://newsapi.org/v2/everything?'
    parameters = {
        'q': 'Colorado', # query phrase
        'pageSize': 20,  # maximum is 100
        'apiKey': key # your own API key
    }
    response = requests.get(url, params=parameters)
    response_json = response.json()
    text = ''
    for i in response_json['articles']:
        text += i['title'] + ' '

    wordcloud = WordCloud(max_font_size=40).generate(text)
    return wordcloud

track = 1
count = 0
def levelOrder(root):
    h = height(root)
    for i in range(1,h+1):
        currentLevel(root,i)
    return count

def currentLevel(root,level):
    if root is None:
        return
    if level == 1:
        global track
        global count
        count = count + (root.data[1] * track)
    elif level > 1:
        currentLevel(root.leftChild, level-1)
        currentLevel(root.rightChild, level-1)

def height(node):
    if node is None:
        return 0
    else:
        leftheight = height(node.leftChild)
        rightheight = height(node.rightChild)
        if (leftheight > rightheight):
            return leftheight+1
        else:
            return rightheight+1

#https://www.geeksforgeeks.org/optimal-binary-search-tree-dp-24/
def OST(keys, frequency, n):
    cost = [[0 for x in range(n)]for y in range(n)]
    for i in range(n):
        cost[i][i] = frequency[i]
    for L in range(2, n + 1):
        for i in range(n - L + 2):
            j = i + L - 1
            off_set_sum = Sum(frequency, i, j)
            if i >= n or j >= n:
                break
            cost[i][j] = 999999999999
            for r in range(i, j + 1):
                c = 0
                if (r > i):
                    c += cost[i][r - 1]
                if (r < j):
                    c += cost[r + 1][j]
                c += off_set_sum
                if (c < cost[i][j]):
                    cost[i][j] = c
    return cost[0][n - 1]

def optCost(frequency, i, j): 
    if j < i:
        return 0
    if j == i:
        return frequency[i]
    fsum = Sum(frequency,i,j)
    minimum = 999999999999
    for r in range(i,j+1):
        cost = (optCost(frequency,i,r-1) + optCost(frequency,r+1,j))
        if cost < minimum:
            minimum = cost
    return minimum + fsum

def OBST(keys,frequency,n):
    return optCost(frequency, 0, n-1)

def Sum(frequency,i,j):
    s = 0
    for k in range(i,j+1):
        s += frequency[k]
        return s

bst = BST()
keys = []
frequency = []
words = API()
listofwords = dict(sorted(words.words_.items(), key = itemgetter(1), reverse = True))
dictList = list(listofwords.items())
random.shuffle(dictList)
for tuple in dictList:
    bst.insert(tuple)
    keys.append(tuple[0])
    frequency.append(tuple[1])
frequency = sorted(frequency, key = float)
lenOfKeys = len(keys)
print(f"Cost of BST: {levelOrder(bst.root)}")
print(f"Cost of the OBST: {OST(keys,frequency,lenOfKeys)}")
plot.figure()
plot.imshow(words, interpolation="bilinear")
plot.axis("off")
plot.show()