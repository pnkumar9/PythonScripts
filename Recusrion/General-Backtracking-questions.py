#!/usr/bin/env python3

#Combinations :
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


#Permutations I
class Solution:
    def permute(self, nums):
        res = []
        self.dfs_PI(nums, [], res)
        return res

    def dfs_PI(self, nums, path, res):
        if not nums:
            res.append(path)
            #return # backtracking
        for i in range(len(nums)):
            self.dfs_PI(nums[:i]+nums[i+1:], path+[nums[i]], res)


#Permutations II
def permuteUnique(self, nums):
    res, visited = [], [False]*len(nums)
    nums.sort()
    self.dfs_PII(nums, visited, [], res)
    return res
    
def dfs_PII(self, nums, visited, path, res):
    if len(nums) == len(path):
        res.append(path)
        return 
    for i in range(len(nums)):
        if not visited[i]: 
            if i>0 and not visited[i-1] and nums[i] == nums[i-1]:  # here should pay attention
                continue
            visited[i] = True
            self.dfs_PII(nums, visited, path+[nums[i]], res)
            visited[i] = False


#Subsets 1
def subsets1(self, nums):
    res = []
    self.dfs_ssI(sorted(nums), 0, [], res)
    return res
    
def dfs_ssI(self, nums, index, path, res):
    res.append(path)
    for i in range(index, len(nums)):
        self.dfs_ssI(nums, i+1, path+[nums[i]], res)


#Subsets II
def subsetsWithDup(self, nums):
    res = []
    nums.sort()
    self.dfs_ssII(nums, 0, [], res)
    return res
    
def dfs_ssII(self, nums, index, path, res):
    res.append(path)
    for i in range(index, len(nums)):
        if i > index and nums[i] == nums[i-1]:
            continue
        self.dfs_ssII(nums, i+1, path+[nums[i]], res)


#Combination Sum
def combinationSum(self, candidates, target):
    res = []
    candidates.sort()
    self.dfs_csI(candidates, target, 0, [], res)
    return res
    
def dfs_csI(self, nums, target, index, path, res):
    if target < 0:
        return  # backtracking
    if target == 0:
        res.append(path)
        return 
    for i in range(index, len(nums)):
        self.dfs_csI(nums, target-nums[i], i, path+[nums[i]], res)



#Combination Sum II
def combinationSum2(self, candidates, target):
    res = []
    candidates.sort()
    self.dfs_csII(candidates, target, 0, [], res)
    return res
    
def dfs_csII(self, candidates, target, index, path, res):
    if target < 0:
        return  # backtracking
    if target == 0:
        res.append(path)
        return  # backtracking 
    for i in range(index, len(candidates)):
        if i > index and candidates[i] == candidates[i-1]:
            continue
        self.dfs_csII(candidates, target-candidates[i], i+1, path+[candidates[i]], res)