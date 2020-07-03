#!/usr/bin/env python3.6

def binarySearch(array, target):
    left  = 0
    right = len(array) - 1
	
    while left <= right:
        mid = (left + right) //2
        
        potentialMatch = array[mid]
        
        if target == potentialMatch:
            return mid
        elif target < potentialMatch:
            right = mid - 1
        else:
            left = mid + 1
            
    return -1		

print(binarySearch([0, 1, 21, 33, 45, 45, 61, 71, 72, 73],33))    