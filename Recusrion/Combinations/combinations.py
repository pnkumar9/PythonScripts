#!/usr/bin/env
'''
77. Combinations
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

Example:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
'''

class Solution():
    def combine(self, n, k):
        res = []
        self.dfs(range(1,n+1), k, 0, [], res)
        return res
        
    def dfs(self, nums, k, index, path, res):
        #if k < 0:  #backtracking
            #return 
        if k == 0:
            res.append(path)
            return # backtracking 
        for i in range(index, len(nums)):
            self.dfs(nums, k-1, i+1, path+[nums[i]], res)    


p = Solution()
print(p.combine(4, 2))            