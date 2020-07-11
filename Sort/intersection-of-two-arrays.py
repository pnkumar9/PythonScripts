#!/usr/bin/env python3.6

'''
Given two arrays, write a function to compute their intersection.
Each element is result must be unique.

Input: 
nums1 = [1,2,2,1], nums2 = [2,2]
Output: 
[2]
'''

# ****** NOTE: the following two solutions fail if len(arr2) > len(arr1) *****
# see third solution for the better one
#use "import counter from collections"
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


#print(intersection_of_two_arrays([1,2,2,1], [2,2]))    


'''
Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Note:

Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.
'''

def intersection_of_two_arrays_II(arr1, arr2):


    #now check if arr2 contains elements in arr1_set
    intersection = []
    for num in arr2:
        if num in arr1:
            intersection.append(num)

    return(intersection)           


#print(intersection_of_two_arrays_II([1,2,2,1], [2,2]))  

#Best solution using Counter method from collections module

from collections import Counter
def intersection_of_two_arrays_III(arr1, arr2):


        c1, c2 = Counter(arr1), Counter(arr2)
        print(c2)
        result = []
        for k1 in c1:
            if k1 in c2:
                rf = min(c1[k1], c2[k1])
                result.extend([k1]*rf)
        return result 

#print(intersection_of_two_arrays_III([1,2,2,1], [2,2])) 
print(intersection_of_two_arrays_III([2,2,4], [1,2,2,3,4,1]))