# similary as stack we can use list to implement this but that is not the most feasible
# we use collection deque() to make a queue

from collections import deque
queue = deque()

queue.appendleft(5)
queue.appendleft(7)
queue.appendleft(90)

queue.pop()
#output 5
class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self,val):
        self.buffer.appendleft(val)

    def dequeue(self):
        return self.buffer.pop()

    def is_empty(self):
        return len(self.buffer)==0

    def size(self):
        return len(self.buffer)


queue = Queue()

queue.enqueue({
    'company': 'Wall Mart',
    'timestamp': '15 apr, 11:02 AM',
    'price': 132
})
queue.enqueue({
    'company': 'Wall Mart',
    'timestamp': '15 apr, 11:03 AM',
    'price': 134
})
queue.enqueue({
    'company': 'Wall Mart',
    'timestamp': '15 apr, 11:04 AM',
    'price': 130
})

queue.dequeue()
