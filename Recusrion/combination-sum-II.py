#!/usr/bin/env python3
'''
40. Combination Sum II
Given a collection of candidate numbers (candidates) and a target number (target), 
find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]

Example 2:

Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]
'''

'''
SOlution is same as combination sum I, only change here is
in case of same element just take first one and ignore rest of the elements

'''
def combination_sum_II(s, targetsum):
    result = []
    s.sort()
    helper(s, 0, targetsum, [], 0, result)
    return result

def helper(s, i, targetsum, slate, slatesum, result):
    #back tracking
    if slatesum > targetsum:
        return

    #back tracking
    if slatesum == targetsum:
        result.append(slate)
        return

    #base case
    if i == len(s):
        return

    #recursive case
    for pick in range(i, len(s)):
        # Very important here! We don't use `i > 0` because we always want 
        # to count the first element in this recursive step even if it is the same 
        # as one before. To avoid overcounting, we just ignore the duplicates
        # after the first element.        
        if pick > i  and s[pick] == s[pick-1]:
            continue

        helper(s, pick+1, targetsum, slate+[s[pick]], slatesum+s[pick], result)

print(combination_sum_II([10,1,2,7,6,1,5], 8))
print(combination_sum_II([2,5,2,1,2], 5))