#!/usr/bin/env python3.6
'''
Heap queue is a special tree structure in which each parent node is less than or equal to its child node. 
In python it is implemented using the heapq module. 
It is very useful is implementing priority queues where the queue item with higher weight is given more priority in processing.

Create a Heap
A heap queue is created by using python’s inbuilt library named heapq. This library has the relevant functions to carry out various operations on a heap data structure. Below is a list of these functions.

heapify – This function converts a regular list to a heap. In the resulting heap the smallest element gets pushed to the index position 0. But rest of the data elements are not necessarily sorted.
heappush – This function adds an element to the heap without altering the current heap.
heappop – This function returns the smallest data element from the heap.
heapreplace – This function replaces the smallest data element with a new value supplied in the function.
'''
# Definition for singly-linked list.
class ListNode(object):
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next

        # defining comparators less_than and equals
        def __lt__(self, other):
            return self.val < other.val

        def __eq__(self, other):
            if(other == None):
                return False
            if(not isinstance(other, ListNode)):
                return False
            return self.val == other.val            

def printList(head):
    while head:
        print(head.val, end="->")
        head = head.next
    print(None)        


import heapq
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return None
        heap = []
        dummy = ListNode(0)
        head = dummy
        print(lists)
        for node in lists:
            if node is not None:
                heap.append((node.val, node))
                print(heap)
        heapq.heapify(heap)
        while heap:
            _, curNode = heapq.heappop(heap) ## _ Ignore  value when unpacking
            print("inside while loop",curNode, heap[0])
            head.next = curNode
            head = head.next
            if curNode.next:
                heapq.heappush(heap,(curNode.next.val,curNode.next))
        return dummy.next	
        
if __name__ == '__main__':
    k=3
    #create this linked list and send as input
    #[[1,4,5],[1,3,4],[2,6]]
    A = [ListNode]*k

    A[0] = ListNode(1)
    A[0].next = ListNode(4)
    A[0].next.next = ListNode(5)

    A[1] = ListNode(1)
    A[1].next = ListNode(3)
    A[1].next.next = ListNode(4)

    A[2] = ListNode(2)
    A[2].next = ListNode(6)

    p1 = Solution()
    head = p1.mergeKLists(A)
    printList(head)
