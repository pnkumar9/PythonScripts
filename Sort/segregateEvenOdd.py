#!/usr/bin/env python3.6

'''
Input  = {12, 34, 45, 9, 8, 90, 3}
Output = {12, 34, 8, 90, 45, 9, 3}
1) Initialize two index variables left and right:  
            left = 0,  right = size -1 
2) Keep incrementing left index until we see an odd number.
3) Keep decrementing right index until we see an even number.
4) If lef < right then swap arr[left] and arr[right]
'''

def segregateEvenOdd(arr):

    left,right=0,len(arr)-1

    while left < right:
        while ((arr[left] %2 == 0) and (left < right)):
            left += 1

        while ((arr[right] %2 == 1) and (left < right)):
            right -= 1

        if left < right :
            swap(left, right, arr)
            left += 1
            right -= 1
    return arr


def swap(i,j,arr):
    arr[i], arr[j] = arr[j], arr[i]
# This is fastest solution
def solve(arr):
    j = 0;
    for i in range(0, len(arr)):
        if arr[i] % 2 == 0:
            swap(i, j, arr);
            j += 1;
    return arr;

print(segregateEvenOdd([12, 34, 45, 9, 8, 90, 3]))
print(solve([12, 34, 45, 9, 8, 90, 3]))