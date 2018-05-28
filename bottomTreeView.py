class bstNode():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
class binaryTree():
    def __init__(self, value):
        self.root = bstNode(value)

    def add(self, value):
        temp = self.root
        while True:
            if temp.value > value:
                if temp.left is None:
                    temp.left = bstNode(value)
                    break
                else:
                    temp = temp.left
            else:
                if temp.right is None:
                    temp.right = bstNode(value)
                    break
                else:
                    temp = temp.right

def bottomTreeView(node):
    st = ""
    if node.left is not None:
        st += bottomTreeView(node.left)
    if node.left is None or node.right is None:
        st += str(node.value)
    if node.right is not None:
        st += bottomTreeView(node.right)
    return st

bTree = binaryTree(5)
bTree.add(3)
bTree.add(7)
bTree.add(2)
bTree.add(4)
bTree.add(6)
bTree.add(8)
print bottomTreeView(bTree.root)



