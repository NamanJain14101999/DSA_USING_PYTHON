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

def stock(arr):
    stack = Stack()
    result = []
    for i in range(0,len(arr)):
        if stack.is_empty():
            result.append(-1)
        elif not stack.is_empty():
            while (not stack.is_empty() and arr[i]>stack.peek()[0]):
                stack.pop()
            if stack.is_empty():
                result.append(-1)
            else:
                result.append(stack.peek()[1])
        stack.push([arr[i],i])
    ans=[]
    print(result)
    for item,enum in enumerate(result):
        ans.append(item-enum)
    return ans

arr = [80,90,100]
print(stock(arr)) 