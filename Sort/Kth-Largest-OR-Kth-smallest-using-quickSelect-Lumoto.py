#!/usr/bin/env python3

# Please see Quick-Sort.py and understand how quick sort with random index works

# Fundamentals of Kth larget or smallest array
# if an array of size n is sorted:
#           1st larget element is at: n-1 index
#           2nd larget element is at: n-2 index
#           3rd larget element is at: n-3 index
#           Kth larget element is at: n-k index
#*******************************
#           1st smallet element is at: 0th index (1-1)
#           2nd smallet element is at: 1st index (2-1)
#           3rd smallet element is at: 2nd index (3-1)
#           kth smallet element is at: (k-1)th index (k-1)

# use quick select is have O(n) time

def KthLargetElement(nums, k):
    helper(nums, 0, len(nums)-1, len(nums)-k)
    print(f"{k}th larget element is: {nums[(len(nums))-k]}")
    return nums[(len(nums))-k]

def KthSmallestElement(nums, k):    
    helper(nums, 0, len(nums)-1, k-1)
    print(f"{k}th smallest element is: {nums[k-1]}")
    return nums[k-1]    

import random
def helper(A, start, end, index):
    if start == end:
        return
    #print(f"incoming array: {A}")
    #Do Lumoto's partition

    ## choose random pivot
    random_index = random.randint(start, end)

    # move pivot to beginning of list
    swap(start, random_index, A)

    #now start partioning left of the elements

    orange = start
    pivot = A[start]

    for green in range(start+1, end+1): #This is crucial start+1..end+1
        if A[green] < pivot:
            orange += 1
            swap(orange, green, A)

    # move pivot to correct location
    swap(start, orange, A)

    #now pivot index is at organge
    #print(f"partioned array: {A} Now pivot index is at: {orange} len(nums)-k: {index}")

    # recursively partition one side only
    if index == orange:
        #print("equal")
        return
    elif index < orange:
        #print("calling left array")
        #call left array
        helper(A, start, orange-1, index)
    else:
        #print("calling right array")
        helper(A, orange+1, end, index)        

def swap(i, j, A):
    A[i] , A[j] = A[j], A[i]

print(KthLargetElement([2,7,5,1,9,10,17], 3))
print(KthSmallestElement([2,7,5,1,9,10,17], 3))