#!/usr/bin/env python3.6

'''
***** Best Solution
YOU should understand this to understand ThreeNumberSum
'''

def twoNumberSum1(array, targetSum):
    	
	array.sort()
	
	left = 0
	right = len(array)-1
	
	while left < right:
		currSum = array[left] + array[right]
		if currSum == targetSum:
			return [array[left], array[right]]
		elif currSum < targetSum:
			left += 1
		elif currSum > targetSum:
			right -= 1
			
	return []			



def twoNumberSum(array, targetSum):
    
	#create empty dict
	nums = {}
	
	for num in array:
		potentialMatch = targetSum - num
		if potentialMatch in nums:
			return [potentialMatch,num]
		else:
			nums[num] = True
			
	return []

'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''
import collections
def twoSum(nums, target):
	
	num_dict = collections.defaultdict()

	for index, num in enumerate(nums):
		
		pMatch = target - num
		
		if pMatch not in num_dict:
			num_dict[num] = index
		else:
			return [num_dict[pMatch], index]
			
	return []    

print(twoNumberSum([1,2,3,1],3))
print(twoSum([1,2,3,1],3))