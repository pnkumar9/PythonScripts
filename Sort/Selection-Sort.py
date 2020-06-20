#!/usr/bin/env python3.6

'''
Selection sort
pass 0 : select min value for the element 0
pass 1 : select min value for the element 1

Tip: if sorting is needed in increasing order
     use condition arr[i] > a[j]

     if you need decreasing order, use condition arr[i] < arr[j]
'''

def selection_sort(arr):

    if len(arr) < 1:
        return arr

    for i in range(len(arr)):
        print (f"i : {i}")
        for j in range(i+1, len(arr)):
            print (f"j : {j}")
            if arr[i] < arr[j]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp

    print(arr)

selection_sort([2,7,5,1,9])    