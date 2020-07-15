#!/usr/bin/env python3
'''
39. Combination Sum
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
Example 2:

Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
'''

def combination_sum_I(s, targetsum):
    result = []
    s.sort()
    helper(s, 0, targetsum, [], 0, result)
    return result

def helper(s, i, targetsum, slate, slatesum, result):
    #base case
    if slatesum > targetsum:
        return

    if slatesum == targetsum:
        result.append(slate)
        return

    #base case
    if i == len(s):
        return

    #recursive case
    for pick in range(i, len(s)):
        helper(s, pick, targetsum, slate+[s[pick]], slatesum+s[pick], result)


print(combination_sum_I([2,3,6,7], 7))
print(combination_sum_I([2,3,5], 8))