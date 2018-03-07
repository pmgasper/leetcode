#!/usr/bin/env python3
#
# Design a stack that supports push, pop, top, and retrieving the minimum
# element in constant time.
#


class MinStack:

    def __init__(self):
        self.stack = []
        self.min = []

    def push(self, x):
        ''' Push element x onto stack '''
        self.stack.append(x)

        if self.min:
            self.min.append(min(x, self.min[-1])) 
        else:
            self.min.append(x) 

    def pop(self):
        ''' Removes the element on top of the stack'''
        if self.stack:
            self.stack.pop()
            self.min.pop()

    def top(self):
        ''' Get the top element '''
        if self.stack:
            return self.stack[-1]
        else:
            return None

    def get_min(self):
        ''' Retrieve the minimum element in the stack'''
        if self.min:
            return self.min[-1]
        else:
            return None


# Tests
obj = MinStack()
print(obj.top(), obj.get_min()) # None, None
obj.push(5)
print(obj.top(), obj.get_min()) # 5, 5
obj.push(7)
obj.push(3)
print(obj.top(), obj.get_min()) # 3, 3
obj.pop()
print(obj.top(), obj.get_min()) # 7, 5
print(obj.top(), obj.get_min()) # 7, 5
obj.pop()
obj.pop()
obj.pop()
obj.pop()
obj.pop()
print(obj.top(), obj.get_min()) # None, None

