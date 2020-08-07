#!/usr/bin/env python3.6

'''
'''
class Solution2(object):
    def mergeKLists(self, lists):
        if not lists:
            return 
        if len(lists) == 1:
            return lists[0]
        mid = len(lists)//2
        l = self.mergeKLists(lists[:mid])
        r = self.mergeKLists(lists[mid:])
        return self.merge(l, r)

    def merge(self, l, r):
        dummy = cur = ListNode(0)
        while l and r:
            if l.val < r.val:
                cur.next = l
                l = l.next
            else:
                cur.next = r
                r = r.next
            cur = cur.next
        cur.next = l or r
        return dummy.next

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
