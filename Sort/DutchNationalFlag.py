#!/usr/bin/env python3.6

'''
Given an array A[] consisting 0s, 1s and 2s. 
The task is to write a function that sorts the given array. 
The functions should put all 0s first, then all 1s and all 2s in last.

example:
Input: {0, 1, 2, 0, 1, 2}
Output: {0, 0, 1, 1, 2, 2}

Input: {0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1}
Output: {0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2}

conditions: time must be O(n)
https://www.youtube.com/watch?v=sEQk8xgjx64

3-way partion
'''

def dutchNationalFlag(arr):

    l=m=0
    r = len(arr) - 1

    while m <= r:
        if arr[m] == 0:
            swap(m, l, arr)
            l += 1
            m += 1
            #print(f" 0 case: {l}{m}{r}")
        elif arr[m] == 1:
            m += 1
            #print(f" 1 case: {l}{m}{r}")
        elif arr[m] == 2:
            swap(m, r, arr)
            r -= 1
            #print(f" 2 case: {l}{m}{r}")

    #print(arr)
    return arr

def swap(i, j, arr):
    arr[i], arr[j] = arr[j], arr[i]

print(dutchNationalFlag([0, 1, 2, 0, 1, 2]))    