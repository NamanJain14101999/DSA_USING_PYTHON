class Node:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None

def height(node):
    if node is None:
        return 0
    else:
        lheight=height(node.left)
        rheight=height(node.right)

        if lheight>rheight:
            return lheight+1
        else:
            return rheight+1

rootnode=Node(10)
rootnode.left=Node(20)
rootnode.right=Node(30)
rootnode.left.left=Node(40)

print(height(rootnode))