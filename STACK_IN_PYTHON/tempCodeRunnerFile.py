'''
using deque as stack
'''
from collections import deque
stack=deque()
stack.append("a")
stack.append("b")
stack.append('c')
stack.append("d")
print(stack)
stack.pop()
print(stack)
stack.pop()
print(stack)
