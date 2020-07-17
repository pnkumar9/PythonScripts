#!/usr/bin/env python3
'''
131. Palindrome Partitioning
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

Example:

Input: "aab"
Output:
[
  ["aa","b"],
  ["a","a","b"]
]
'''
class Solution():
    def partition(self, s):
        res = []
        self.dfs(s, [], res)
        return res
        
    def dfs(self, s, slate, res):
        if not s: # backtracking
            #res.append("|".join(slate[:]))
            res.append(slate[:])
        # take every possible string from the current position and 
        # if it's palndromic go forward, and if it's not prune            
        for i in range(1, len(s)+1):
            if self.isPar(s[:i]):
                self.dfs(s[i:], slate+[s[:i]], res)
                
    def isPar(self, s):
        return s == s[::-1]

p = Solution()
print(p.partition("aab"))


#uplevel version
def helper( s, slate, res):
    
    #backtrack
    if not s:
        res.append("|".join(slate[:]))
        
    for i in range(1, len(s)+1):
        if isPal(s[:i]):
            helper(s[i:], slate+[s[:i]], res)
        

def isPal(s):
    return s == s[::-1] 
    
def generate_palindromic_decompositions(s):
    res = []
    helper(s, [], res)
    return res