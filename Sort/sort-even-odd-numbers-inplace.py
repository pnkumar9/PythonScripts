#!/usr/bin/python

'''
Given an array of integers (both odd and even), sort them in such a way that the first part of the array 
contains even numbers  rest portion contains odd numbers .
'''

def even_odd(nums):

    if len(nums) == 0:
        return []
    elif len(nums) == 1:        
        return nums

    next_even, next_odd = 0, len(nums)-1

    while next_even < next_odd:
        if nums[next_even] %2 == 0:
            next_even += 1
        else:
            nums[next_even], nums[next_odd] = nums[next_odd], nums[next_even]
            next_odd -= 1


nums = [1,2,3,4,5,6,7,8,9,10,11,12,13]
even_odd(nums)
print(nums)            

'''
Given an array of integers (both odd and even), sort them in such a way that the first part of the array 
contains even numbers in ascending order  rest portion contains odd numbers in descending order .
'''
def even_odd_with_sort(nums):

    if len(nums) == 0:
        return []
    elif len(nums) == 1:        
        return nums

    next_even, next_odd = 0, len(nums)-1
    # Count of number of
    # odd numbers, used in
    # slicing the array later.
    k = 0

    while next_even < next_odd:
        if nums[next_even] %2 == 0:
            next_even += 1
            k += 1
        else:
            nums[next_even], nums[next_odd] = nums[next_odd], nums[next_even]
            next_odd -= 1

    #now nums is partitioned with even and odd

    evens = nums[:k]
    odds = nums[k:]

    evens.sort()
    odds.sort(key=None, reverse=True)

    evens.extend(odds)

    return evens

nums = [1,2,3,4,5,6,7,8,9,10,11,12,13]
print(even_odd_with_sort(nums))
       