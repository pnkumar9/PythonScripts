#!/usr/bin/env python3.6

# The Sound of Sorting Algorithms in Python's Taste # 
 
# 1 
def bubble_sort(seq): 
    """ worst(n^2), best(n), avg(n^2) 
        stable: yes 
    """ 
    for passnum in range(len(seq) - 1, 0, -1): 
        for i in range(passnum): 
            if seq[i] > seq[i + 1]: 
                seq[i], seq[i + 1] = seq[i + 1], seq[i] 
 
# 2 
def selection_sort(seq): 
    """ worst(n^2), best(n^2), avg(n^2) 
        stable: no 
    """ 
    for i in range(len(seq) - 1): 
        mini, miniat = seq[i], i 
        for j in range(i + 1, len(seq)): 
            if seq[j] < mini: mini, miniat = seq[j], j 
        seq[i], seq[miniat] = seq[miniat], seq[i] 
 
# 3 
def ins_sort(seq): 
    """ worst(n^2), best(n), avg(n^2) 
        stable: yes 
    """ 
    for i in range(1, len(seq)): 
        j = i 
        while j > 0 and seq[j - 1] > seq[j]: 
            seq[j - 1], seq[j] = seq[j], seq[j - 1] 
            j -= 1 
 
# 4 
def partition(seq): 
    pi, seq = seq[0], seq[1:] 
    lo = [x for x in seq if x <= pi] 
    hi = [x for x in seq if x > pi] 
    return lo, pi, hi 
 
def quicksort(seq): 
    """ worst(n^2), best(n lgn), avg(n lgn) 
        stable: no 
    """ 
    if len(seq) <= 1: return seq 
    lo, pi, hi = partition(seq) 
    return quicksort(lo) + [pi] + quicksort(hi) 
 
# 5 
def mergesort(seq): 
    """ worst(n lgn), best(n lgn), avg(n lgn) 
        stable: yes 
    """ 
    mid = len(seq) // 2 
    lft, rgt = seq[:mid], seq[mid:] 
    if len(lft) > 1: lft = mergesort(lft) 
    if len(rgt) > 1: rgt = mergesort(rgt) 
    res = [] 
    while lft and rgt: 
        if lft[-1] >= rgt[-1]: 
            res.append(lft.pop()) 
        else: 
            res.append(rgt.pop()) 
    res.reverse() 
    return (lft or rgt) + res 
 
# 6 
def heapify(seq, i, n): 
    l, r = 2 * i + 1, 2 * (i + 1) 
    maxat = i 
    if l <= n and seq[l] > seq[i]: 
        maxat = l 
    if r <= n and seq[r] > seq[maxat]: 
        maxat = r 
    if maxat != i: 
        seq[i], seq[maxat] = seq[maxat], seq[i] 
        heapify(seq, maxat, n) 
 
def buildheap(seq, s, n): 
    for i in range(s, -1, -1): 
        heapify(seq, i, n) 
 
def heapsort(seq): 
    """ worst(n lgn), best(n lgn), avg(n lgn) 
        stable: no 
    """ 
    end = len(seq) - 1 
    start = end / 2 
    buildheap(seq, start, end) 
 
    for i in range(end, 0, -1): 
        seq[0], seq[i] = seq[i], seq[0] 
        end -= 1 
        heapify(seq, 0, end) 