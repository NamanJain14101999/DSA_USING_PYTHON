from collections import deque
class Stack:
    def __init__(self):
        self.stack=deque()

    def push(self,data):
        self.stack.append(data)
    
    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def is_empty(self):
        return (self.stack)==0
    
    def size(self):
        return len(self.stack)

s=Stack()
s.push(10)
s.push(20)
s.push(30)
s.push(40)



    

