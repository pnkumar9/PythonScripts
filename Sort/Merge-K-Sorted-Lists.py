#!/usr/bin/env python3.6

'''
'''

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

        #we need this when we pull out everything from minheap
        dummy = ListNode(0)
        head = dummy

        #dump all the K lists into minheap
        for node in lists:
            if node is not None:
                heap.append((node.val, node))
        heapq.heapify(heap)


        while heap:
            _, curNode = heapq.heappop(heap)
            head.next = curNode
            head = head.next
            if curNode.next:
                heapq.heappush(heap,(curNode.next.val,curNode.next))
        return dummy.next	

class ListNode(object):
    def __init__(self, value):
        self.value = value
        self.nextnode = None
