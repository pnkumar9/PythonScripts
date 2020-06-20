#!/usr/bin/env python3.6

'''
Bubble sort

scan from left to right
compare side by side elements

idea : largest element will bubbled up to UP (right side)

input is our zip code 2 7 5 1 9

pass 1
  (2 7) 5 1 9 --> compare 2,7 for 2<7 if yes NO SWAP, if no SWAP --> 2 7 5 1 9
  2 (7 5) 1 9 --> compare 7,5 (swap) --> 2 5 7 1 9
  2 5 (7 1) 9 --> compare 7,1 (swap) --> 2 5 1 7 9
  2 5 1 (7 9) --> compare 7,9 (no swap)

Every position 'i' will be compared with 'i+1' position in every pass
pass 2
  2 5 1 7 9
'''

def bubble_sort(arr):

  for i in range(len(arr)):
    for j in range(len(arr)-1):
      if arr[j] > arr[j+1]:
        temp = arr[j]
        arr[j] = arr[j+1]
        arr[j+1] = temp

  print(arr)        

bubble_sort([2,7,5,1,9])
bubble_sort([7,4,3,2,0])
