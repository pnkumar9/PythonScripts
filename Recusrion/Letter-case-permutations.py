#!/usr/bin/env python3

'''
Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string.  Return a list of all possible strings we could create.

Examples:
Input: S = "a1b2"
Output: ["a1b2", "a1B2", "A1b2", "A1B2"]

Input: S = "3z4"
Output: ["3z4", "3Z4"]

Input: S = "12345"
Output: ["12345"]
'''

'''
Reference:
https://leetcode.com/problems/letter-case-permutation/discuss/379928/Python-clear-solution
'''

def letterCasePermutations(s):
    result = []
    helper(s, 0, "", result)
    return result


def helper(input, i,  slate, result):

    if i >= len(input):
        result.append(slate)
        #print(result)
    else:
        if input[i].isdigit():
            helper(input, i+1, slate + input[i], result)
        else:
            helper(input, i+1, slate + input[i].lower(), result)
            helper(input, i+1, slate + input[i].upper(), result)


print(letterCasePermutations('a1b1'))
print(letterCasePermutations('3z4'))
print(letterCasePermutations('12345'))
print('\n')

def letterCasePermutationsII(s):
    result = []
    helperII(s, 0, "", result)
    return result


def helperII(input, i,  slate, result):

    if i >= len(input):
        result.append(slate)
        #print(result)
    else:
        if input[i].isdigit():
            helper(input, i+1, slate + input[i], result)
        else:
            helper(input, i+1, slate + input[i].swapcase(), result)

print(letterCasePermutations('a1b1'))
print(letterCasePermutations('3z4'))
print(letterCasePermutations('12345'))