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