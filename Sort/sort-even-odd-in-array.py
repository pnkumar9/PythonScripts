'''
Sort all even numbers in ascending order and then sort all odd numbers in descending order
Last Updated: 03-12-2019
Given an array of integers (both odd and even), sort them in such a way that the first part of the array contains odd numbers sorted in descending order, rest portion contains even numbers sorted in ascending order.

Examples:

Input  : arr[] = {1, 2, 3, 5, 4, 7, 10}
Output : arr[] = {7, 5, 3, 1, 2, 4, 10}

Input  : arr[] = {0, 4, 5, 3, 7, 2, 1}
Output : arr[] = {7, 5, 3, 1, 0, 2, 4} 
'''

# Python program to sort array 
# in even and odd manner 
# The odd numbers are to be 
# sorted in descending order 
# and the even numbers in 
# ascending order 

# To do two way sort. First 
# sort even numbers in ascending 
# order, then odd numbers in 
# descending order. 
def two_way_sort(arr, arr_len): 
	
	# Current indexes l->left 
	# and r->right 
	l, r = 0, arr_len - 1
	
	# Count of number of 
	# odd numbers, used in 
	# slicing the array later. 
	k = 0
	
	# Run till left(l) < right(r) 
	while(l < r): 
		
		# While left(l) is odd, if yes 
		# increment the left(l) plus 
		# odd count(k) if not break the 
		# while for even number found 
		# here to be swaped 
		while(arr[l] % 2 != 0): 
			l += 1
			k += 1
			
		# While right(r) is even, 
		# if yes decrement right(r) 
		# if not break the while for 
		# odd number found here to 
		# be swaped	 
		while(arr[r] % 2 == 0 and l < r): 
			r -= 1
			
		# Swap the left(l) and right(r), 
		# which is even and odd numbers 
		# encountered in above loops 
		if(l < r): 
			arr[l], arr[r] = arr[r], arr[l] 
			
	# Slice the number on the 
	# basis of odd count(k) 
	odd = arr[:k] 
	even = arr[k:] 
	
	# Sort the odd and 
	# even array accordingly 
	odd.sort(reverse = True) 
	even.sort() 
	
	# Extend the odd array with 
	# even values and return it. 
	odd.extend(even) 
	
	return odd 
	
# Driver code 
arr_len = 6
arr = [1, 3, 2, 7, 5, 4] 
result = two_way_sort(arr, arr_len) 
for i in result: 
	print(str(i) + " "), 

# This code is contributed 
# by JaySiyaRam 

#=========== using list comprehension ========#
# Function to Sort even-placed elements 
# in increasing and odd-placed in decreasing 
# order 

def evenOddSort(input): 

	# separate even odd indexed elements list 
	evens = [ input[i] for i in range(0,len(input)) if i%2==0 ] 
	odds = [ input[i] for i in range(0,len(input)) if i%2!=0 ] 

	# sort evens in ascending and odds in 
	# descending using sorted() method 
	print (sorted(evens) + sorted(odds,reverse=True)) 

# Driver program 
if __name__ == "__main__": 
	input = [0, 1, 2, 3, 4, 5, 6, 7] 
	evenOddSort(input) 
