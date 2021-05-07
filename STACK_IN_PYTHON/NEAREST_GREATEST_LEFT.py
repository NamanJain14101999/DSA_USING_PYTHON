from collections import deque
class Stack:
    def __init__(self):
        self.stack = deque()  

    def push(self,data):
        self.stack.append(data)

    def pop(self):
        if self.is_empty():
            raise Exception('Stack Underflow')
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            return None
        return  self.stack[-1]

    def is_empty(self):
        return len(self.stack)==0
    
    def size(self):
        return len(self.stack)

def nearest_greater_to_left(arr):
    stack = Stack()
    result = []
    for i in range(0,len(arr)):
        if stack.is_empty():
            result.append(-1)
        elif not stack.is_empty():
            while(not stack.is_empty() and arr[i] > stack.peek()):
                stack.pop()
            if stack.is_empty():
                result.append(-1)
            else:
                result.append(stack.peek())
        stack.push(arr[i])
    return result

arr = [24,11,13,21,3]

print(nearest_greater_to_left(arr))