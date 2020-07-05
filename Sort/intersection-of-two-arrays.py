#!/usr/bin/env python3.6

'''
Given two arrays, write a function to compute their intersection.
Each element is result must be unique.

Input: 
nums1 = [1,2,2,1], nums2 = [2,2]
Output: 
[2]
'''

def intersection_of_two_arrays(arr1, arr2):

    # load all the elements in arr1 into set , which takes care of removing duplicates
    arr1_set = set()
    for i in arr1:
        arr1_set.add(i)

    print(arr1_set)

    #now check if arr2 contains elements in arr1_set
    intersection = set()
    for num in arr2:
        if num in arr1_set:
            intersection.add(num)

    return(list(intersection))            


print(intersection_of_two_arrays([1,2,2,1], [2,2]))    


