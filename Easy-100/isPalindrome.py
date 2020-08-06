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
    
    str1 = ''.join(e.lower() for e in s if e.isalnum())
    #print(str1)

    return str1 == str1[::-1]
     

      


print(isPalindrome2("A man, a plan, a canal: Panama"))  
print(isPalindrome2("race a car"))   