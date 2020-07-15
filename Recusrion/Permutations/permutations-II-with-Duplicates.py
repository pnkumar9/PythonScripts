#!/usr/bin/env python3
'''
47. Permutations II
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:

Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
'''

class Solution1(object):
    def permuteUnique(self, s):
        result = []
        self.helper(s, 0, result)
        return result

    def swap(self, i, j, s):
        s[i], s[j] = s[j], s[i]

    def helper(self, s, i, result):
        #base case
        if i == len(s):
            result.append(s[:])
        else:
            #recursive case
            hmap = {}
            for pick in range(i, len(s)):
                if s[pick] not in hmap:
                    hmap[s[pick]] = 1
                    self.swap(pick, i, s)
                    self.helper(s, i+1, result)
                    self.swap(pick, i, s)
                

p = Solution1()
print(p.permuteUnique([1,1,2]))
