from collections import deque
def N_G_R(arr):   # in n^2
    result=[]
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            if arr[i]<arr[j]:
                result.append(arr[j])
                break
        else:
            result.append(-1)
    return result
  
# in n

class Stack():
    def __init__(self):
        self.stack=deque()
    
    def push(self,data):
        self.stack.append(data)
        
    def is_empty(self):
        return len(self.stack)==0
    
    def pop(self):
        if self.is_empty():
            return "stack is empty"
        else:
            return self.stack.pop()

    def peek(self):
        if self.is_empty():
            return "stack is empty"
        else:
            return self.stack[-1]

def neartest_greatest_right(arr):
    stack=Stack()
    result=[]
    for i in range(len(arr)-1,-1,-1):
        if stack.is_empty():
            result.append(-1)
        elif not stack.is_empty():
            while (not stack.is_empty() and arr[i]>stack.peek()):
                stack.pop()
            if stack.is_empty():
                result.append(-1)
            else:
                result.append(stack.peek())
                
        stack.push(arr[i])

    result.reverse()
    return result

a=[24,11,13,21,3]


print(neartest_greatest_right(a))