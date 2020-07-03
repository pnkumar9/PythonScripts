#!/usr/bin/env python3.6

'''
Given an array of integers, find the first missing positive integer in linear time and constant space. 
In other words, find the lowest positive integer that does not exist in the array. 
The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

1. Since the first missing positive number must be between 1 and len(array) + 1 (why?), we can ignore any negative numbers and numbers bigger than len(array). 

2. e can do this is by adding all the numbers to a set, and then use a counter initialized to 1. 
  Then continuously increment the counter and check whether the value is in the set.

  Input [3, 4, -1, 1] , here if we ignore 0 and -ve number, postive number must be between 1 and len(nums)+1
'''

def first_missing_positive(nums):
    seen = set(nums)
    i = 1
    while i in seen:
        i += 1
    return i


print(first_missing_positive([3, 4, -1, 1]))

print(first_missing_positive([1,2,0]))

print(first_missing_positive([99,-202,43,0]))