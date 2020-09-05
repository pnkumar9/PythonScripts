'''
14. Longest Common Prefix
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
'''
def longestCommonPrefix(strs):
    """
    :type strs: List[str]; rtype: str
    """
    sz, ret = zip(*strs), ""
    #('f', 'f', 'f')
    #('l', 'l', 'l')
    #('o', 'o', 'i')

    for c in sz:
        print(c)
        if len(set(c)) > 1: break
        ret += c[0]
    return ret

print(longestCommonPrefix(["flower","flow","flight"]))