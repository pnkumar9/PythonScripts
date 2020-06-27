#!/usr/bin/env python3.6

def ins_sort(seq): 
    """ worst(n^2), best(n), avg(n^2) 
        stable: yes 
    """ 
    for i in range(1, len(seq)): 
        j = i 
        while j > 0 and seq[j - 1] > seq[j]:
            swap(j-1, j, seq)
            j -= 1

    print(seq)        

def swap(i,j,arr):
      arr[i], arr[j] = arr[j], arr[i]
           

ins_sort([2,7,5,1,9])
ins_sort([7,4,3,2,0])