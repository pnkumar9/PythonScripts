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
    #back track case
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


#print(combination_sum_I([2,3,6,7], 7))
#print(combination_sum_I([2,3,5], 8))


#FIX This
# following code failed for inputs 
# [10,20] target 0
# [-5, -10] target -15
# [-3,-3,-3,-3] target -12
# [-10000000000,-10000000000,-80000000000,-30000000000,-180000000000,110000000000,60000000000] target -90000000000

def check_if_sum_possible(arr, k):
    arr.sort()
    res = []
    find = False
    dfs(arr, k, 0, [], res)
    if len(res) > 0:
        find = True
    return find
    

def dfs(candidates, target, index, path, res):
    if target < 0:
        return  # backtracking
    
    if len(candidates) == 1:
        if target == candidates[0]:
            res.append(candidates[0])
            return
        else:
            return
    
    if target == 0 and index > 0:
        res.append(path)
        return  # backtracking 
    
    
    for i in range(index, len(candidates)):
        dfs(candidates, target-candidates[i], i, path+[candidates[i]], res)

#print(check_if_sum_possible([10,20], 0))
#print(check_if_sum_possible([-5, -10], -15))


def combination_sum_I_for_UL(s, targetsum):
    result = []
    s.sort()
    find = False
    helper_UL(s, 0, targetsum, [], 0, result)
    if len(result) > 0:
        find = True
    return find

def helper_UL(s, i, targetsum, slate, slatesum, result):
    #back track case
    #if slatesum > targetsum and s[i] > 0:
    #    return

    if slatesum == targetsum and i > 0:
        result.append(slate)
        return

    #base case
    if i == len(s):
        return

    #recursive case
    for pick in range(i, len(s)):
        helper(s, pick, targetsum, slate+[s[pick]], slatesum+s[pick], result)


print(combination_sum_I_for_UL([10,20], 0))
print(combination_sum_I_for_UL([-5, -10], -15))
