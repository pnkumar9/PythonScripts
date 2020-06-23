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


print(twoNumberSum([1,2,3,1],3))