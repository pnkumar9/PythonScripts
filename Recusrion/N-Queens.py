#!/usr/bin/env python3

class Solution():
    def solveNQueens(self, n):
        res = []
        self.dfs([-1]*n, 0, [], res)
        return res
    
    # nums is a one-dimension array, like [1, 3, 0, 2] means
    # first queen is placed in column 1, second queen is placed
    # in column 3, etc.
    def dfs(self, nums, index, slate, res):
        if index == len(nums):
            res.append(slate)
            return  # backtracking
        for i in range(len(nums)):
            nums[index] = i
            if self.valid(nums, index):  # pruning
                tmp = "."*len(nums)
                self.dfs(nums, index+1, slate+[tmp[:i]+"Q"+tmp[i+1:]], res)

    # check whether nth queen can be placed in that column
    def valid(self, nums, n):
        for i in range(n):
            #Do they lie along the same diagonal? nums[i] == nums[n]
            #Do they lie in same column? (row difference) == (column difference)
            #nums[index] --> columns
            #index --> row
            #abs(nums[i]-nums[n] -- > distance between columns
            # n-i --> distance between rows
            #if abs(nums[i]-nums[n]) == n -i or nums[i] == nums[n]:
            if abs(nums[i]-nums[n]) == n -i or nums[i] == nums[n]:
                return False
        return True

p = Solution()
print(p.solveNQueens(4))        