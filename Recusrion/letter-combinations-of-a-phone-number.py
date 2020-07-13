#!/usr/bin/env python3

'''
17. Letter Combinations of a Phone Number
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Although the above answer is in lexicographical order, your answer could be in any order you want.

'''
def letterCombinations(digits):
    if not digits:
        return []
    dic = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
    res = []
    dfs(digits, dic, 0, "", res)
    return res

def dfs(digits, dic, index, path, res):
    if len(path) == len(digits):
        res.append(path)
        return
    
    # 2 --> abc 3 --> def
    for j in dic[digits[index]]:
        dfs(digits, dic, index+1, path+j, res)


print(letterCombinations('23'))        