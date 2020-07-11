#!/usr/bin/env python3.6

'''
Quickselect Algorithm
Quickselect is a selection algorithm to find the k-th smallest element in an unordered list. It is related to the quick sort sorting algorithm.

Examples:

Input: arr[] = {7, 10, 4, 3, 20, 15}
           k = 3
Output: 7

Input: arr[] = {7, 10, 4, 3, 20, 15}
           k = 4
Output: 10
The algorithm is similar to QuickSort. The difference is, instead of recurring for both sides (after finding pivot), 
it recurs only for the part that contains the k-th smallest element. 
The logic is simple, if index of partitioned element is more than k, then we recur for left part. 
If index is same as k, we have found the k-th smallest element and we return.
 If index is less than k, then we recur for right part. 
 This reduces the expected complexity from O(n log n) to O(n), with a worst case of O(n^2).
'''
# Python3 program of Quick Select 

# Standard partition process of QuickSort(). 
# It considers the last element as pivot 
# and moves all smaller element to left of 
# it and greater elements to right 
def partition(arr, l, r): 
	
	x = arr[r] 
	i = l 
	for j in range(l, r): 
		
		if arr[j] <= x: 
			arr[i], arr[j] = arr[j], arr[i] 
			i += 1
			
	arr[i], arr[r] = arr[r], arr[i] 
	return i 

import sys
# finds the kth position (of the sorted array) 
# in a given unsorted array i.e this function 
# can be used to find both kth largest and 
# kth smallest element in the array. 
# ASSUMPTION: all elements in arr[] are distinct 
def kthSmallest(arr, left, r, k): 
  
    # if k is smaller than number of 
    # elements in array 
    if (k > 0 and k <= r - left + 1): 
  
        # Partition the array around last 
        # element and get position of pivot 
        # element in sorted array 
        print(f"input arr: {arr} K: {k}")
        index = partition(arr, left, r)
        print(f"index: {index} arr: {arr} K: {k}") 
  
        # if position is same as k 
        if (index - left == k - 1):
            print(f"returning: {arr[index]} arr: {arr}")  
            return arr[index] 
  
        # If position is more, recur  
        # for left subarray  
        if (index - left > k - 1):
            print("calling left sub array: {arr[left:index - 1]} k: {k}") 
            return kthSmallest(arr, left, index - 1, k) 
  
        # Else recur for right subarray
        print("calling right sub array: {arr[index + 1: r]} k: {k - index + left - 1}")  
        return kthSmallest(arr, index + 1, r,  
                            k - index + left - 1) 
    return sys.maxsize 

# Driver Code 
#arr = [ 10, 4, 5, 8, 6, 11, 26 ] 
arr = [7, 10, 4, 3, 20, 15]
n = len(arr) 
k = 4
print("K-th smallest element is ", end = "") 
print(kthSmallest(arr, 0, n - 1, k)) 

# This code is contributed by Muskan Kalra. 
     
            
"""
Another version
QuickSelect finds the kth smallest element of an array in mostly linear time.
"""
import random

def Partition(a):
  """
  Usage: (left,pivot,right) = Partition(array)
  Partitions an array around a randomly chosen pivot such that 
  left elements <= pivot <= right elements.
  Running time: O(n)
  """
  ## Base cases
  if len(a)==1: 
    return([],a[0],[])
  if len(a)==2: 
    if a[0]<=a[1]:
      return([],a[0],a[1])
    else:
      return([],a[1],a[0])
  ## Choose a random pivot
  p = random.randint(0,len(a)-1)  ## the pivot index
  pivot = a[p]  ## the pivot value
  right = []    ## the right partition
  left = []     ## the left partition
  for i in range(len(a)):
    if not i == p:
      if a[i] > pivot:
        right.append(a[i])
      else:
        left.append(a[i])
  return(left, pivot, right)
  
def QuickSelect(a,k):
  """
  Usage: kth_smallest_element = QuickSelect(array,k)
  Finds the kth smallest element of an array in linear time.
  """
  (left,pivot,right) = Partition(a)
  if len(left)==k-1:   ## pivot is the kth smallest element
    result = pivot
  elif len(left)>k-1: ## the kth element is in the left partition
    result = QuickSelect(left,k)
  else:               ## the kth element is in the right partition
    result = QuickSelect(right,k-len(left)-1)
  return result     