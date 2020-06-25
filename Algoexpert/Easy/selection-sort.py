#!/usr/bin/env python3.6

def selectionSort(array):
    
	currIdx = 0
	
	while currIdx < len(array) - 1:
		
		minIdx = currIdx
		#iterate thru starting from currIdx+1 to find exact mindIdx
		for i in range(currIdx+1, len(array)):
			if array[minIdx] > array [i]:
				minIdx = i
		
		#after every pass get mindIdx and replace with first element in unsorted portion of the array
		swap(currIdx, minIdx, array)
		#increase while loop counter
		currIdx += 1
		
	return array
		
def swap(i,j,array):
	array[i], array[j] = array[j], array[i]


print(selectionSort([8, 5, 2, 9, 5, 6, 3]))    