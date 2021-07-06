from collections import deque

class Queue:
    def __init__(self):
        self.queue=deque()
    def enqueue(self,data):
        self.queue.appendleft(data)
    def dequeue(self):
        if self.isemplty():
            return False
        else:
             return self.queue.pop()
    def is_empty(self):
        return len(self.queue) ==0 
    def size(self):
        return len(self.queue)
    def print_queue(self):
        print(self.queue)

pq= Queue()
pq.enqueue(100)
pq.enqueue(200)
pq.enqueue(300)
pq.print_queue()
print(pq.size())
print(pq.dequeue())
print(pq.dequeue())
