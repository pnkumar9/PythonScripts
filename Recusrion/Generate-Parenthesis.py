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

def helper(numLefParan, numRightParan, slate, result):
    #backtrack case
    if numLefParan > numRightParan:
        return

    #base case
    if numRightParan == 0 and numLefParan == 0:
        result.append("".join(slate[:]))

    #recursive case
    if numLefParan > 0:
        helper(numLefParan-1, numRightParan, slate+['('], result)

    if numRightParan > 0:
        helper(numLefParan, numRightParan-1, slate+[')'], result)        

def generate_paranthesis(n):
    result = []
    helper(n, n, [], result)
    return result

print(generate_paranthesis(3))    