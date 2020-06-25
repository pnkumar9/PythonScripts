#!/usr/bin/env python3.6
'''
given two arry of ints
Determine if second array is subsequence of the first one

subsequence not necessarily adjacent in the array but that are in the same order
as they appear in the array.

ex: number [1,3,4] form subsequence of [1,2,3,4]
'''
def isValidSubsequence(array, sequence):
    arrIdx = 0
    SeqIdx = 0
    while arrIdx < len(array) and SeqIdx < len(sequence):
        if array[arrIdx] == sequence[SeqIdx]:
            SeqIdx += 1
        arrIdx += 1
    return SeqIdx == len(sequence)

print(isValidSubsequence([5, 1, 22, 25, 6, -1, 8, 10],  [1, 6, -1, 10]))