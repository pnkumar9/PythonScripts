#!/usr/bin/env python3.6

def twoSumHash(arr, k):

    seen = set()

    for num in arr:

        target = k - num
        if target not in seen:
            seen.add(num)
        else:
            return [num, target]

    return []                        


def findZeroSum(arr):
    # Write your code here.
    arr.sort()
    output = []

    #print(arr[-1])
    for i in range(len(arr)-2):
        if (i==0 or arr[i]!=arr[i-1]):
            left =  i+1
            right = len(arr)  - 1   
    
            while left < right:
                currsum = arr[i] + arr[left] + arr[right]

                if currsum == 0:
                    output.append(f'{arr[i]},{arr[left]},{arr[right]}')
                    left += 1
                    right -= 1
                    while left < right and arr[left] == arr[left-1]:
                        left += 1
                    while left < right and arr[right] == arr[right+1]:
                        right -= 1                    
                elif currsum < 0:
                    left += 1
                elif currsum > 0:
                    right -= 1
            
                
    return output    

#print(twoSumHash([10, 15, 3, 7,10], 17))

#print(findZeroSum([10, 3, -4, 1, -6, 9]))
#print(findZeroSum([0,0,0,0,0,0,0]))
#print(findZeroSum([6,-1,-1,0,0,1,1]))

def merge_sort(arr):
    #base case
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    
    L = arr[:mid]
    R = arr[mid:]
    
    merge_sort(L)
    merge_sort(R)
    
    i=j=k=0
    
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    
    #This case covers if array sizes are different
    while i < len(L):
        arr[k] = L[i]
        i+=1
        k+=1
        
    while j < len(R):
        arr[k] = R[j]
        j+=1
        k+=1
        
        
    return arr   

#print(merge_sort([1,7,5,3]))    
#print(merge_sort([1]))
from heapq import heapify,heappushpop 
def kLargestElements(arr,k):
    res = list(set(arr))
    heap = res[:k]

    print(res)

    heapify(heap)

    for i in range(k,len(res)):
        #print(f"i: {i} ")
        if res[i] > heap[0]:
            heappushpop(heap, res[i])
            
    return heap		    

print(kLargestElements([1, 5, 4, 4, 2], 3))    