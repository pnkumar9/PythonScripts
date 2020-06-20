#!/usr/bin/env python3.6

'''
Merge two sorted arrays with different size

a = [1,3,5,7,9]
b = [2,4,6,8,10,12,14,16]

result should be [1..10,12,14,16]

ref: https://www.youtube.com/watch?v=xF3TU-QlhJQ
'''

def merge_two_sorted_arrays(a,b):

    i=0
    j=0
    k=0
    result = []
    # scan untill at lease one array is finished
    while (i < len(a) and j < len(b)):
        #print(f"i: {i} and j: {j} and k: {k}")
        #print(f"a[i]: {a[i]} and b[j]: {b[j]}")
        if a[i] < b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1

    if i < len(a):
        result += a[i:]

    if j < len(b):
        result += b[j:]

    print(result)

merge_two_sorted_arrays([1,3,5,7,9], [2,4,6,8,10,12,14,16])
