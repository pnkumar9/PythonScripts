'''
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

Follow up: Could you write an algorithm with O(log n) runtime complexity?

 

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]

when it says log(n) that means it is binary search but it's modified binary search in this case
Better explained here: https://www.youtube.com/watch?v=bU-q1OJ0KWw
'''

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        result = [-1,-1]
        result[0] = self.findStartingIndex(nums, target)
        result[1] = self.findendingIndex(nums, target)
        return result

    def findStartingIndex(self, nums, target):
        index = -1
        start = 0
        end = len(nums)-1
        while(start <= end):
            midpoint = start + (end-start)//2
            if nums[midpoint] >= target:
                end = midpoint -1
            else:
                start = midpoint + 1
            
            if nums[midpoint] == target:
                index = midpoint
            
        return index
    
    def findendingIndex(self, nums, target):
        index = -1
        start = 0
        end = len(nums)-1
        while(start <= end):
            midpoint = start + (end-start)//2
            if nums[midpoint] <= target:
                start = midpoint + 1
            else:
                end = midpoint -1
            
            if nums[midpoint] == target:
                index = midpoint
            
        return index