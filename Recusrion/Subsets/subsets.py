#!/usr/bin/env python3

'''
78. Subsets
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
'''

'''
This is same as letter case permutations problem but with a change

use include , exlude stratgey

left child slate will be as it is i.e. NO addition
right child appends slate


'''

def subsets(nums):
    result = []
    slate = []
    helper(nums, 0, slate, result)
    return result


def helper(input, i,  slate, result):

    if i == len(input):
        result.append(slate)
        #print(result)
    else:
        helper(input, i+1, slate, result) # exlclude element for left child
        helper(input, i+1, slate+[input[i]], result) # include element for right child


print(subsets([1,2,3]))    

#uplevel
def generate_all_subsets(s):
    
    
    def helper(s, i, slate, res):
        
        #base case
        if i == len(s):
            res.append(slate)
        else:
            helper(s, i+1, slate, res)
            helper(s, i+1, slate+s[i], res)
        
    
    #use include exclude tree
    res = []
    helper(s, 0, "", res)
    return res