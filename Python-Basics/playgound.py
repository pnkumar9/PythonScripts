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

    
    for i in range(len(arr)-2):
        
        left =  i+1
        right = len(arr)  - 1   

        while left < right:
            currsum = arr[i] + arr[left] + arr[right]
            #print(f"currsum: {currsum} three numbers: {arr[i],arr[left],arr[right]}" )
            
            if currsum == 0:
                output.append((arr[i], arr[left], arr[right]))
                left += 1
                right -= 1
            elif currsum < 0:
                left += 1
            elif currsum > 0:
                right -= 1
                
    return output     

#print(twoSumHash([10, 15, 3, 7,10], 17))

print(findZeroSum([10, 3, -4, 1, -6, 9]))