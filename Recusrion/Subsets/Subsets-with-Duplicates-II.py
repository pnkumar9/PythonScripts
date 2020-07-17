#!/usr/bin/env python3
'''
90. Subsets II
Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
'''

def helper(s, index, slate, result):
  #base case
  result.append(slate[:])

  # Recursive case
  for i in range(index,len(s)):
      if i != index and s[i] == s[i-1]: continue
      helper(s, i+1, slate+[s[i]], result)




def subsets_with_duplicates(s):
  result = []
  #pre-sort the array
  s.sort()
  helper(s, 0, [], result)
  return result

print(subsets_with_duplicates([1,2,2]))