#!/usr/bin/env python3.6

def partition(arr):
    pi, seq = arr[0], arr[1:]
    lo = [x for x in seq if x <= pi]
    hi = [x for x in seq if x > pi]

    return lo, pi, hi

# recursive function, please write base case first
def quicksort(arr):

    #base case
    if len(arr) <= 1:
        return arr
    # partition the incoming array
    lo, pi, hi = partition(arr)

    return quicksort(lo) + [pi] + quicksort(hi)

print(quicksort([2,7,5,1,9,10,17]))    



   