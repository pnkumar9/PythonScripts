#!/usr/bin/env python3.6

callnum = 0


# Python program for implementation of MergeSort 
def mergeSort1(arr): 
	global callnum
	callnum += 1
	print(f"call number {callnum} and input array is {arr}")
	if len(arr) >1: 
		mid = len(arr)//2 # Finding the mid of the array 
		L = arr[:mid] # Dividing the array elements 
		R = arr[mid:] # into 2 halves 

		print("calling L")
		mergeSort1(L) # Sorting the first half 
		print("calling R")
		mergeSort1(R) # Sorting the second half 

		i = j = k = 0
		print(f" Sort started L: {L} R: {R}")
		# Copy data to temp arrays L[] and R[] 
		while i < len(L) and j < len(R): 
			if L[i] < R[j]: 
				arr[k] = L[i] 
				i+= 1
			else: 
				arr[k] = R[j] 
				j+= 1
			k+= 1
		
		# Checking if any element was left 
		while i < len(L): 
			arr[k] = L[i] 
			i+= 1
			k+= 1
		
		while j < len(R): 
			arr[k] = R[j] 
			j+= 1
			k+= 1
		print(f" Sort Ended Result: {arr}")

# Code to print the list 
def printList(arr): 
	for i in range(len(arr)):		 
		print(arr[i], end =" ") 
	print() 

def mergeSort_with_aux_array(arr):
    if len(arr) == 1:
        return arr
    else:
        a = arr[:len(arr)/2]
        b = arr[len(arr)/2:]
        a = mergeSort(a)
        b = mergeSort(b)
        c = []
        i = 0
        j = 0
        while i < len(a) and j < len(b):
            if a[i] < b[j]:
                c.append(a[i])
                i = i + 1
            else:
                c.append(b[j])
                j = j + 1
        c += a[i:]
        c += b[j:]
    return c

# driver code to test the above code 
if __name__ == '__main__': 
	arr = [12, 11, 13, 5, 6, 7] 
	print ("Given array is", end ="\n") 
	printList(arr) 
	mergeSort1(arr) 
	print("Sorted array is: ", end ="\n") 
	printList(arr) 

# This code is contributed by Mayank Khanna 

