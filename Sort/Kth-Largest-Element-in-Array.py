#!/usr/bin/env python3.6

# This algo uses min heap

# 1. Buid miniheap for the K numbers
# 2. keep adding rest of the elements only if the element is > root (min heap root is always minimum value)
# 3. Kth largest element is heap[0]

from heapq import heapify, heappushpop

class Solution:
    def findKthLargest(self, nums, k):
        heap = nums[:k]
        print(heap)
        heapify(heap)
        
        for i in range(k, len(nums)):
            if nums[i] > heap[0]:
                heappushpop(heap, nums[i])
        
        return heap[0]


#  1,2,9,12,23,30,50
print(Solution().findKthLargest([1, 23, 12, 9, 30, 2, 50], 4))        