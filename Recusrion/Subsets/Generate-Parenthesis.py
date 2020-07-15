#!/usr/bin/env python3

'''
22. Generate Parentheses
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
'''
class Solution():
    def generateParenthesis(self, n):
        res = []
        self.dfs(n, n, "", res)
        return res
            
    def dfs(self, leftRemain, rightRemain, path, res):
        if leftRemain > rightRemain or leftRemain < 0 or rightRemain < 0:
            return  # backtracking
            #backtracking
        if leftRemain == 0 and rightRemain == 0:
            res.append(path)
            return 
        self.dfs(leftRemain-1, rightRemain, path+"(", res)
        self.dfs(leftRemain, rightRemain-1, path+")", res)
p = Solution()
print(p.generateParenthesis(3))    