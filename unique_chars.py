#!/usr/bin/env python3.6

'''
Unique Characters in String
Problem
Given a string,determine if it is compreised of all unique characters. 
For example, the string 'abcde' has all unique characters and should return True. 
The string 'aabcde' contains duplicate characters and should return false.
'''

# Two solutions for this problem

def unique_chars_1(s):
    return(len(set(s)) == len(s))

def unique_chars_2(s):

    s_temp = set()

    for char in s:
        if char in s_temp:
            return False
        else:
            s_temp.add(char)

    return True

print (unique_chars_1("ABCDE"))
print (unique_chars_2("ABCDEFF"))                


