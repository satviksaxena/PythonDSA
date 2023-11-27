# we do not use list for stacks because list is dynamic and it will increase in size and
# we will not be able to do arr[-1]
# and arr.pop()

# use collections library
from collections import deque
stack = deque()
dir(stack)

# We can use dequeue fuctions but here we have implemented more things on top of that
# TODO: study the deque collection

class Stack:
    def __init__(self):
        self.container = deque()

    def push(self,value):
        self.container.append(val)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container)==0

    def size(self):
        return len(self.container)

stk = Stack ()
stk.push(5)
stk.peek()