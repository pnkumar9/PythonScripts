#!/usr/bin/env python3.6

def isPal(s):
    if len(s) <= 1:
        return True
    else:
        print (s[0],s[-1])
        return s[0] == s[-1] and isPal(s[1:-1])

print (isPal("heeeeh"))