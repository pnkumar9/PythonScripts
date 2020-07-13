#!/usr/bin/env python3

mystr = "My name is Kumar"
print(mystr.strip()[::-1])

'''
using recursive method
'''
def reverseString(s) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    def helper(start, end, s):

        if start >= end:
            return

        swap(start, end, s)

        return helper(start+1, end-1, s)

    def swap(i, j, s):
        s[i], s[j] = s[j], s[i]
    
    helper (0, len(s)-1, s)
    print(s)


print(reverseString(["h","e","l","l","o"]))    