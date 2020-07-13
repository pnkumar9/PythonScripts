#!/usr/bin/env python3

'''
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), 
find the count of all unique combinations in candidates where the candidate numbers sums to target.

Input: candidates = [2,3,4,6,7], target = 7,
Output: 2

because
A solution set is:
[
  [7],
  [4,3]
]
'''

'''
use include/exclude recursive method
'''
def combination_sum(nums, targetSum):
    return helper(nums, targetSum, 0, 0)


def helper(input, targetSum,  i, slateSum):

    if slateSum == targetSum:
        return 1
    if (i == len(input)) or (slateSum > targetSum):
        return 0
        #print(result)
    
    return ( helper(input, targetSum, i+1, slateSum) + 
             helper(input, targetSum, i+1, slateSum+input[i]) ) # include element for right child


print(combination_sum([1,2,3], 3))   
print(combination_sum([2,3,4, 6,7], 7))             