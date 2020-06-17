#!/usr/bin/env python3.6

'''
Deques are a generalization of 
stacks and queues (the name is pronounced “deck” and is short for “double-ended queue”). 
Implement a Deque
Finally, implement a Deque class! It should be able to do the following:

Check if its empty
Add to both front and rear
Remove from Front and Rear
Check the Size

 like a queue <--[1,2,3,4,5] --> like a stack
 rear is at the index 0 which is 1 in the example
 front is len-1 which is 5 in the example

 Add to the right : use extend,append
 delete from right: pop

 add to left : extend left,appendleft,
 remove from left: popleft
'''

class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0,item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)