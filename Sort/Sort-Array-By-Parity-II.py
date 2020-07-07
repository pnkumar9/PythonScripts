#!/usr/bin/env python3

'''
922. Sort Array By Parity II
Given an array A of non-negative integers, half of the integers in A are odd, and half of the integers are even.

Sort the array so that whenever A[i] is odd, i is odd; and whenever A[i] is even, i is even.

You may return any answer array that satisfies this condition.
 

Example 1:

Input: [4,2,5,7]
Output: [4,5,2,7]
Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.
 

Note:

2 <= A.length <= 20000
A.length % 2 == 0
0 <= A[i] <= 1000
'''

# brute force takes O(n**2)

# solution should be in in-place

# we use two pointers method, one for even index and second one for odd index
def sortArrayByParityII(A):
    even = 0
    odd = 1
    lenA = len(A)
    while (even < lenA and odd < lenA):

        # traverse the even indices untill you hit odd number
        while (even < lenA and (A[even] % 2 == 0) ):
            even += 2

        # traverse the odd indices untill you hit even number
        while (odd < lenA and (A[odd] % 2 == 1) ):
            odd += 2

        # check indices boundaries and swap elements
        if(even < lenA and odd < lenA):
            swap(even, odd, A)

    return A

def swap(i, j, A):
    A[i], A[j] = A[j], A[i]

print(sortArrayByParityII([4,2,5,7]))    

