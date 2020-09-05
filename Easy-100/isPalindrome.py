#!/usr/bin/env python3

def is_palindrome(string):
    if not string or len(string) == 1:
        return True

    low, high = 0, len(string) - 1
    while low < high:
        if string[low] != string[high]:
            return False
        low += 1
        high -= 1

    return True

import re
def isPalindrome2(s):
    
    cleaned_s = "".join(c for c in s if c.isalnum()).lower()
    #print(str1)

    return cleaned_s == cleaned_s[::-1]
     
def isPalindrome3(self, s):
    l, r = 0, len(s) - 1
    while l < r:
        if not s[l].isalnum():
            l += 1
        elif not s[r].isalnum():
            r -= 1
        else:
            if s[l].lower() != s[r].lower():
                return False
            else:
                l += 1
                r -= 1
    return True
      


print(isPalindrome2("A man, a plan, a canal: Panama"))  
print(isPalindrome2("race a car"))   