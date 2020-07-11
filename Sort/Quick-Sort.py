#!/usr/bin/env python3.6

import random
def partition(arr):
    pi, seq = arr[0], arr[1:]
    lo = [x for x in seq if x <= pi]
    hi = [x for x in seq if x > pi]

    return lo, pi, hi

def partition_random(arr):
    pindex = random.randrange(0, len(arr)-1)
    arr[0] , arr[pindex] = arr[pindex], arr[0]
    pi, seq = arr[0], arr[1:]
    lo = [x for x in seq if x <= pi]
    hi = [x for x in seq if x > pi]

    return lo, pi, hi

# recursive function, please write base case first
def quicksort(arr):

    #base case, MUST cover size 0 or 1 case
    if len(arr) <= 1:
        return arr
    # partition the incoming array
    #lo, pi, hi = partition(arr)
    print("calling partition_random")
    lo, pi, hi = partition_random(arr)

    return quicksort(lo) + [pi] + quicksort(hi)

print(quicksort([2,7,5,1,9,10,17]))

# LUMOTO's quick sort with random pivot instead of arr[0] as pivot.
# Understand this method to write Kth, Larget or Kth Smallest coding problems

    # Generating a random number between the  
    # starting index of the array and the 
    # ending index of the array. 
    #randpivot = random.randrange(start, stop) 

import random

def quicksort_lumoto(arr):
    pass





   