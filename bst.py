'''
Binary Search tree implementation
'''

class node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class bst():
    def __init__(self):
        self.head = None
    
    def insert(self, value):
        if self.head is None:
            self.head = node(value)
        else:
            temp = self.head
            found = False
            while not False:
                if temp is None:
                    temp = node(value)
                    found = True
                if temp.value > value:
                    temp = temp.left
                else:
                    temp = temp.right

    def find(self, value):
        found = False
        temp = self.head
        parent = None
        while not found:
            if temp is None:
                return 'Not Found'
            else:
                if temp.value > value:
                    parent = temp
                    temp = temp.left
                elif temp.value < value:
                    parent = temp
                    temp = temp.right
                else:
                    found = True
        return temp, parent

    def findNextGreatest(self, node):
        temp = node
        if node.right is None:
            return  node.left
        else:

    def delete(self, value):
        #will delete the first occurance of that value
        node, parent = self.find(value)
        if node.left is None and node.right is None:
            if parent is None:
                self.head = None
            else:
                if parent.left is node:
                    parent.left = None
                else:
                    parent.right = None
        else:
            if node.right is None:
                # we need to find the left
                if parent.



