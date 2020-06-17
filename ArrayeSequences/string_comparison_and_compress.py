#!/usr/bin/env python3.6

'''
String Compression¶
Problem
Given a string in the form 'AAAABBBBCCCCCDDEEEE' compress it to become 'A4B4C5D2E4'. For this problem, you can falsely "compress" strings of single or double letters. For instance, it is okay for 'AAB' to return 'A2B1' even though this technically takes more space.

The function should also be case sensitive, so that a string 'AAAaaa' returns 'A3a3'.
'''

def string_compare_compress(s):

    print(s)
    # Begin Run as empty string
    r = ""
    l = len(s)
    
    # Check for length 0
    if l == 0:
        return ""

    r = ""
    l = len(s)
    cnt = 1
    i = 1

    if l == 1:
        return s+"1"

    while i < l:
        if s[i] == s[i-1]:
            cnt += 1
        else:
            r = r + s[i-1] + str(cnt)
            cnt = 1
        i = i+1

    return r + s[i-1] + str(cnt)

print(string_compare_compress("AAaaBBB"))
