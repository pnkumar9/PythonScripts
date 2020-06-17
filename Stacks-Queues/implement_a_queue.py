#!/usr/bin/env python3.6

'''
Implement a Queue
It's very common to be asked to implement a Queue class! The class should be able to do the following:

Check if Queue is Empty
Enqueue
Dequeue
Return the size of the Queue
queue is FIFO
'''
class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []
    #adds at the beginning of the queue
    #NOTE: when you add an element at index 0, existing elemnets shift to the right of the list
    def enqueue(self, item):
        self.items.insert(0,item)
    #pops out the end of the queue
    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)        

    def display_queue(self):
        return (self.items)   


q = Queue()
print(q.size())
print(q.enqueue(1))
print(q.enqueue(2))
print(q.enqueue(3))
print(q.size())
print(q.display_queue())
print(q.dequeue())
print(q.size())