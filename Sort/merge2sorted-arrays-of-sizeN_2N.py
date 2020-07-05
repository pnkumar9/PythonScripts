#!/usr/bin/env python3.6

'''
arr1 size is N
arr2 size is 2N
condtions: inplace
no output should be returned but arr2 should be updated.
each element must be checked
half of arr2 are filled with 0s to accomdate sorted elements

ex:
arr1 = [1 3 5]
arr2 = [2 4 6 0 0 0 ]

result:
arr2 = [1 2 3 4 5 6]

concept:
IMP: use 3 pointers, all starts on right side of the array and valid elements only

[1 3 5] [2 4 6 0 0 0 ]
     ^       ^     ^
     |       |     |
     i       j     k

on every pass compare elements at i and j and place high element at index k

keep doing this untill i < 0 and j < 0
decrement pointers accordingly

We cannot start the merge from the beginning of the two arrays, as this will require the movement of the data. 

'''

def mergeSortedArraysSizeNand2N_V1(arr1, arr2):

    i = len(arr1) - 1
    j = (len(arr2) // 2) - 1
    k = len(arr2) - 1

    print(f"{i} {j} {k}")
    while  i >= 0 and j >= 0:
        if arr1[i] > arr2[j]:
            arr2[k] = arr1[i]
            i -= 1
            k -= 1
        else:
            arr2[k] = arr2[j]
            j -= 1
            k -= 1

    while  i >= 0:
        arr2[k] = arr1[i]
        i -= 1
        k -= 1

    while  j >= 0:
        arr2[k] = arr2[j]
        j -= 1
        k -= 1    
    print(arr2)

def mergeSortedArraysSizeNand2N_V2(arr1, arr2):
    
    i = len(arr1) - 1
    j = (len(arr2) // 2) - 1
    k = len(arr2) - 1

    print(f"{i} {j} {k}")
    while  i >= 0:
        if  (j >= 0 ) and (arr2[j] > arr1[i]):            
            arr2[k] = arr2[j]
            j -= 1
            k -= 1            
        else:
            arr2[k] = arr1[i]
            i -= 1
            k -= 1

    print(arr2)

mergeSortedArraysSizeNand2N_V1([1,3,5], [2,4,6,0,0,0])    
mergeSortedArraysSizeNand2N_V2([1,3,5], [2,4,6,0,0,0])    
