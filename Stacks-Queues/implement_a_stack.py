#!/usr/bin/env python3.6
'''
A very common interview question is to begin by just implementing a Stack! 
Try your best to implement your own stack!

It should have the methods:

Check if its empty
Push a new item
Pop an item
Peek at the top item
Return the size

whats is stack?
a special type of data structure in which items are removed in the reverse order from that in 
which they are added, so the most recently added item is the first one removed. 
This is also called last-in, first-out (LIFO).

Adding an item to a stack is called pushing. Removing an item from a stack is called popping.
'''
class stack(object):

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return(self.items == [])

    #LIFO, so it adds at the end of the list
    def push(self, item):
        self.items.append(item)

    #modifies the stack
    def pop(self):
        self.items.pop()

    #simply displays last item but don't modify the stack
    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return(len(self.items))


s = stack()        
print(s.size())
print(s.push('1'))
print(s.push(2))
print(s.push(3))
print(s.push(4))
print(s.size())
print(s.peek())
