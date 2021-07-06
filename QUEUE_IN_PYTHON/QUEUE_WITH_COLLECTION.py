from collections import deque

q=deque()
q.appendleft(100)
q.appendleft(200)
q.appendleft(300)
print(q)

q.pop()
print(q)
q.pop()
print(q)
q.pop()
print(q) 