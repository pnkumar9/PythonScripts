#!/usr/bin/env python3.6

'''
segrate even odd numbers
'''

def segregate(arr):

    return [x for x in arr if x %2 == 0] + [x for x in arr if x % 2 == 1]

print(segregate([1,7,9,0,3,6,7,3,1,5,6,7,4]))    

'''
rotate an array by d elements
'''

def rotate(arr, d):
    return arr[d:] + arr[:d]

print(rotate([1,2,3,4,5,6,7,8,9], 3))    

'''
reverse an array
'''

def reverse(arr):
    return arr[::-1]

'''
lambda: anonymous function with capability of holding a single expression only

lambda arguments:expression
'''    

import math

square_root = lambda x: math.sqrt(x)

'''
Map
Map is used in scenarios where we need to apply a function/lambda over a sequence of elements. 
Although you can almost always replace the need for using a map with list comprehensions.
Syntax :-
map(function , sequence)
        - returns an iterable.
'''

import math
arr = [1, 2, 3, 4, 5, 6]
arr = list(map(lambda  x: x**2, arr))

'''
Filter
Filter, on the other hand, applies a function/lambda over a sequence of elements and returns the sequence of elements for which function/lambda returned True.
Syntax :-
    filter(function, sequence)
        - returns an iterable.
'''
arr = [1, 2, 3, 4, 5, 6]
arr = list(filter(lambda x : x%2 == 0, arr))
print (arr)

#Here, we applied filter to return only the even numbers in the sequence.

'''
open file and print lines
for line in open('script.py'):
  print ('line')
'''

