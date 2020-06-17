#!/usr/bin/env python3.6

'''
Doubly Linked List Implementation¶

'''

class DoublyLinkedList(object):

    def __init__(self,value):
        self.value = value
        self.nextnode = None
        self.prevnode = None

a = DoublyLinkedList(1)
b = DoublyLinkedList(2)
c = DoublyLinkedList(3)

# Setting b after a
b.prev_node = a
a.next_node = b

# Setting c after a
b.next_node = c
c.prev_node = b