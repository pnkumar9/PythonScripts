#!/usr/bin/env python3.6

'''
Inversion Count for an array indicates – how far (or close) the array is from being sorted. 
If array is already sorted then inversion count is 0. 
If array is sorted in reverse order that inversion count is the maximum.
Formally speaking, two elements a[i] and a[j] form an inversion if a[i] > a[j] and i < j.

Example:
The sequence 2, 4, 1, 3, 5 has three inversions (2, 1), (4, 1), (4, 3).

These two links have good explanation

https://medium.com/@ssbothwell/counting-inversions-with-merge-sort-4d9910dc95f0
https://www.educative.io/edpresso/how-to-count-the-number-of-inversions-in-an-array


'''

#Brute Force methos , which takes O(n**2)

# Python3 program to count  
# inversions in an array 
  
def getInvCount(arr, n): 
  
    inv_count = 0
    for i in range(n): 
        for j in range(i + 1, n): 
            if (arr[i] > arr[j]): 
                inv_count += 1
  
    return inv_count 

'''
All elements from ‘a’ that are smaller then b[j] are added to ‘c’ before b[j]. 
In other words, the amount of numbers in ‘a’ that are bigger then b[j] is the amount of numbers in ‘a’ 
which have not been appended to ‘c’ yet. We now know that b[j] is in an inversion pair with 
each element of ‘a’ that has not been appended to ‘c’. 
We also know that there are no inversions in ‘b’ because ‘b’ is already sorted! 
Thus we know exactly how many inversions b[j] is a part of.

The iterator ‘i’ already tracks how many elements in ‘a’ have been appended to ‘c’ 
so all we have to do is subtract ‘i’ from the length of ‘a’ and we get this number of inversions 
involving b[j]. If we keep a running tally of len(a)-i for every time 
an element from ‘b’ is smaller then an element in ‘a’ then we know the total number of inversions 
between ‘a’ and ‘b’.
'''
def mergeSortInversions(arr):
    if len(arr) == 1:
        return arr, 0
    else:
        a = arr[:len(arr)/2]
        b = arr[len(arr)/2:]
        a, ai = mergeSortInversions(a)
        b, bi = mergeSortInversions(b)
        c = []
        i = 0
        j = 0
        inversions = 0 + ai + bi
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
            inversions += (len(a)-i)
    c += a[i:]
    c += b[j:]
    return c, inversions    