#!/usr/bin/env python3

def binary_strings(n):
    result = []
    bshelper(n, 0, [], result)
    return result

def bshelper(s, i, slate, result):

    #base case
    if i == s:
        result.append(slate[:])
        return

    #recursove case
    bshelper(s, i+1, slate+[0], result)
    bshelper(s, i+1, slate+[1], result)     

print(binary_strings(3)) 
print(binary_strings(5))       
