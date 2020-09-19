#!/usr/bin/env python3

'''
Finding the median in a list seems like a trivial problem, but doing so in linear time turns out to be tricky.
'''

# Finding the median in O(n log n)

'''
The most straightforward way to find the median is to sort the list and just pick the median by its index. 
The fastest comparison-based sort is O(nlogn), so that dominates the runtime
'''
def nlogn_median(l):
    l = sorted(l)
    if len(l) % 2 == 1:
        return l[len(l) / 2]
    else:
        return 0.5 * (l[len(l) / 2 - 1] + l[len(l) / 2])

#Finding the median in average O(n)        

'''
Pick an index in the list. It doesn’t matter how you pick it, but choosing one at random works well in practice. 
The element at this index is called the pivot.
Split the list into 2 groups:
Elements less than or equal to the pivot, lesser_els
Elements strictly greater than the pivot, great_els
We know that one of these groups contains the median. Suppose we’re looking for the kth element:
If there are k or more elements in lesser_els, recurse on list lesser_els, searching for the kth element.
If there are fewer than k elements in lesser_els, recurse on list greater_els. Instead of searching for k, we search for k-len(lesser_els).
'''

'''
CONCEPT:

Consider the list below. We'd like to find the median.
l = [9,1,0,2,3,4,6,8,7,10,5]
len(l) == 11, so we're looking for the 6th smallest element
First, we must pick a pivot. We randomly select index 3.
The value at this index is 2.

Partitioning based on the pivot:
[1,0,2], [9,3,4,6,8,7,10,5]
We want the 6th element. 6-len(left) = 3, so we want
the third smallest element in the right array

We're now looking for third smallest element in the array below:
[9,3,4,6,8,7,10,5]
We pick an index at random to be our pivot.
We pick index 3, the value at which, l[3]=6

Partitioning based on the pivot:
[3,4,5,6] [9,7,10]
We want the 3rd smallest element, so we know it's the
3rd smallest element in the left array

We're now looking for the 3rd smallest in the array below:
[3,4,5,6]
We pick an index at random to be our pivot.
We pick index 1, the value at which, l[1]=4
Partitioning based on the pivot:
[3,4] [5,6]
We're looking for the item at index 3, so we know it's
the smallest in the right array.

We're now looking for the smallest element in the array below:
[5,6]

At this point, we can have a base case that chooses the larger
or smaller item based on the index.
We're looking for the smallest item, which is 5.
return 5
'''
import random
def quickselect_median(l, pivot_fn=random.choice):
    if len(l) % 2 == 1:
        return quickselect(l, len(l) // 2, pivot_fn)
    else:
        return 0.5 * (quickselect(l, len(l) // 2 - 1, pivot_fn) +
                      quickselect(l, len(l) // 2, pivot_fn))


def quickselect(l, k, pivot_fn):
    """
    Select the kth element in l (0 based)
    :param l: List of numerics
    :param k: Index
    :param pivot_fn: Function to choose a pivot, defaults to random.choice
    :return: The kth element of l
    """
    if len(l) == 1:
        assert k == 0
        return l[0]

    pivot = pivot_fn(l)

    lows = [el for el in l if el < pivot]
    highs = [el for el in l if el > pivot]
    pivots = [el for el in l if el == pivot]

    if k < len(lows):
        return quickselect(lows, k, pivot_fn)
    elif k < len(lows) + len(pivots):
        # We got lucky and guessed the median
        return pivots[0]
    else:
        return quickselect(highs, k - len(lows) - len(pivots), pivot_fn)

print(quickselect_median([7,8,0,4,6,2,3,7,4,9]))