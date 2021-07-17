class BinarySearchTreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

    def add_child(self,data):
        if data == self.data:
            return

        if data<self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)

        if data>self.data:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)
                
    def in_order_traversal(self):
        value=[]
        if self.left:
            value+=self.left.in_order_traversal()
    
        value.append(self.data)

        if self.right:
            value+=self.right.in_order_traversal()

        return value

    def search(self,value):
        if self.data==value:
            return True

        if value<self.data:
            if self.left:
                return self.left.search(value)
            else:
                return False
                
        if value>self.data:
            if self.right:
                return self.right.search(value)
            else:
                return False
    
    def max_tree(self):
        while self.right!=None:
            return self.right.max_tree()
        return self.data
    
    def min_tree(self):
        if self.left is None:
            return self.data
        return self.left.min_tree()

    def delete(self,value):
        if self.data>value:
            if self.left:
                self.left=self.left.delete(value)
        elif value > self.data:
            if self.right:
                self.right=self.right.delete(value)
        else:
            #delete leaf node
            if self.left is None and self.right is None:
                return None
            #delete one child node
            elif self.right is None:
                return self.left
            elif self.left is None:
                return self.right
            #delete two child

            min_val = self.right.min_tree()
            self.data=min_val
            self.right=self.right.delete(min_val)
        return self


def build_tree(numbers):
        print("print tree elements ",numbers)
        root = BinarySearchTreeNode(numbers[0])

        for i in range(1,len(numbers)):
            root.add_child(numbers[i])

        return root

numbers = [17,4,1,20,9,23,8,34]
tree = build_tree(numbers)
print(tree)
print(tree.in_order_traversal())
print(tree.search(20))
print("max element is ,",tree.max_tree())
print(tree.delete(17))
print(tree.in_order_traversal())
