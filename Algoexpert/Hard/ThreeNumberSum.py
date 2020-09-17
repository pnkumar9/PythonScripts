#!/usr/bin/env python3.6
'''
There will be two loops
top for loop is for taking each element for creating sum with rest of any two elements

[2,7,5,1,9,8,0,-2,-4] k =10

start with array[0]
 left = i+1
 right = len(array)-1
 currSum = array[i] + array[left] + array[right]
'''
def threeNumberSum(array, k):
    	#sort the array
	array.sort()
	
	output = []
	
	# len(array) -2 because we are maitaning sum with array[i] + array[left] + array[right]
	for i in range(len(array)-2):
		left = i+1
		right = len(array)-1
		
		while (left < right):
			currSum = array[i] + array[left] + array[right]
			
			if currSum == k:
				output.append([array[i], array[left], array[right]])
				left  += 1
				right -= 1
			elif currSum < k:
				left += 1
			elif currSum > k:
				right -= 1
				
	return output

'''
another version of 3 sum to check if sum=0 a+b+c==0
len(nums)-2 is because we need at least 3 numbers to continue.
if i > 0 and nums[i] == nums[i-1] is because when i = 0, 
it doesn't need to check if it's a duplicate element since it doesn't even have a previous element 
to compare with. And nums[i] == nums[i-1] is to prevent checking duplicate again. 
(This seems to be a good pattern which has been seen in other questions as well).
'''

'''
The way to think about it is since it's 3 sum, there's only going to be 3 numbers. 
So to find the combinations of 3 numbers, he is iterating through the list with the first pointer, 
and then trying to find two extra numbers to sum to 0. Since the list is ordered, the right pointer 
will always be higher than the middle pointer. So if the sum is too large, you can move the right 
pointer back one. On the other hand, if the sum is too small (below 0), then move the middle pointer up one.
'''
class Solution:
def threeSum(self, nums: List[int]) -> List[List[int]]:
	res = []
	nums.sort()
	for i in range(len(nums)-2):
		#If we don't skip this condition, the same results will occur many times which results in failure.
		if i > 0 and nums[i] == nums[i-1]:
			continue
		l, r = i+1, len(nums)-1
		while l < r:
			s = nums[i] + nums[l] + nums[r]
			if s < 0:
				l +=1 
			elif s > 0:
				r -= 1
			else:
				res.append((nums[i], nums[l], nums[r]))
				while l < r and nums[l] == nums[l+1]:
					l += 1
				while l < r and nums[r] == nums[r-1]:
					r -= 1
				l += 1; r -= 1
	return res