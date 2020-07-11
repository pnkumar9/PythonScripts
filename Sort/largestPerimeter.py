#!/usr/bin/env python3

'''
Maximum Perimeter Triangle from array
Given an Array of non-negative integers. Find out three elements from this array which form a triangle of maximum perimeter.

Examples :

Input : {6, 1, 6, 5, 8, 4}
Output : 20

Input : {2, 20, 7, 55, 1, 33, 12, 4}
Output : Triangle formation is not possible.

Input: {33, 6, 20, 1, 8, 12, 5, 55, 4, 9}
Output: 41
'''

'''
concept:
Sort the array of lengths in reverse order. We know that any two sides of a triangle are together greater than the third side. 
So check whether the first length is greater than the sum of the other two. If so, no triangle can be formed and perimeter = 0. 
Continue checking the next 3 lengths. If not, get the sum of the first 3 lengths.
'''
def maxPerimeter(arr): 
    maxi = 0
    n = len(arr) 
    arr.sort(reverse = True) 
  
    for i in range(0, n - 2): 
        if arr[i] < (arr[i + 1] + arr[i + 2]): 
            maxi = max(maxi, arr[i] + 
                       arr[i + 1] + arr[i + 2]) 
            break
  
    if(maxi == 0): 
        return "Triangle formation is not possible"
    else: 
        return "Maximum Perimeter is: "+ str(maxi) 

print(maxPerimeter([6, 1, 6, 5, 8, 4]))
print(maxPerimeter([2, 20, 7, 55, 1, 33, 12, 4]))