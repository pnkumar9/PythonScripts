#!/usr/bin/env python3.6

'''
You are given an integer array nums and you have to return a new counts array. 
The counts array has the property where counts[i] is the 
number of smaller elements to the right of nums[i]

Example:
Given nums = [5, 2, 6, 1]
To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.
Return the array [2, 1, 1, 0].

'''

#brute force method
#Time Complexity: O(n^2)
#Auxiliary Space: O(1)
def constructLowerArray (arr, countSmaller, n): 
  
    # initialize all the counts in countSmaller array as 0  
    for i in range(n):  
        countSmaller[i] = 0;  
  
    for i in range(n): 
        for j in range(i + 1,n): 
            if (arr[j] < arr[i]): 
                countSmaller[i] += 1
# Utility function that prints out an array on a line 
def printArray(arr, size): 
    for i in range(size): 
        print(arr[i],end=" ") 
    print() 

# Driver code  
arr = [12, 10, 5, 4, 2, 20, 6, 1, 0, 2] 
n = len(arr) 
low = [0]*n 
constructLowerArray(arr, low, n) 
printArray(low, n)                 