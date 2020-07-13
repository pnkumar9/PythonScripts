#!/usr/bin/env python3

'''
46. Permutations
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

'''

'''
To understand this draw tree diagram first

'''
class Solution(object):
    def permute(self, s):
        result = []
        self.helper(s, 0, [], result)
        return result

    def swap(self, i, j, s):
        s[i], s[j] = s[j], s[i]

    def helper(self, s, i, slate, result):
        #base case
        if i == len(s):
            #print(f"we hit base case: {nums}")
            result.append(slate[:])
            return

        #recursive case
        for pick in range(i, len(s)):
            #print(f"\nstart-end: {start} to {len(nums)} i:{i} ")
            #print(f"brought num {nums[i]} position {start}")
            self.swap(pick, i, s)
            
            #print(f"nums before backtrack is: {nums}")
            slate.append(s[i])
            self.helper(s, i+1, slate, result)
            slate.pop()
            self.swap(pick, i, s)
            #print(f"nums after backtrack is: {nums}")


p = Solution()
print(p.permute([1,2,3]))

'''
Another easy to understand method
Standard Backtracking Pattern

Use slate to track the permutation so far.
Generate Candidates: for pick in (x for x in s if x not in slate)
Is Solution: len(slate) == len(nums)
'''
class Solution2(object):
    def permute(self, s):
        result = []
        self.helper(s, [], result)
        return result

    def helper(self, s, slate, result):
        #base case
        if len(slate) == len(s):
            result.append(slate[:])
            return

        #recursive case
        for pick in (x for x in s if x not in slate):
            slate.append(pick)
            self.helper(s, slate, result)
            slate.pop()

p = Solution2()
print(p.permute([1,2,3]))
