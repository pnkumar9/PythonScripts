#!/usr/bin/env python3
'''
216. Combination Sum III
Find all possible combinations of k numbers that add up to a number n, 
given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

Note:

All numbers will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: k = 3, n = 7
Output: [[1,2,4]]
Example 2:

Input: k = 3, n = 9
Output: [[1,2,6], [1,3,5], [2,3,4]]
'''

def combination_sum_III(k, n):
    result = []
    
    helper(range(1,10), 0, k, n, [], 0, result)
    return result

def helper(s, i, k, n, slate, slatesum, result):
    #back tracking
    if slatesum > n:
        return

    #base case
    if slatesum == n and len(slate) == k:
        result.append(slate)
        return

    #recursive case
    for pick in range(i, len(s)):
        helper(s, pick+1, k, n, slate+[s[pick]], slatesum+s[pick], result)

print(combination_sum_III(3, 7))
print(combination_sum_III(3, 9))