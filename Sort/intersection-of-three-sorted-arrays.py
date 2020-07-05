#!/usr/bin/env python3.6

'''
Given three integer arrays arr1, arr2 and arr3 sorted in strictly increasing order, return a sorted array of only the integers that appeared in all three arrays.

Example 1:

Input: arr1 = [1,2,3,4,5], arr2 = [1,2,5,7,9], arr3 = [1,3,4,5,8]
Output: [1,5]
Explanation: Only 1 and 5 appeared in the three arrays.
Constraints:

1 <= arr1.length, arr2.length, arr3.length <= 1000
1 <= arr1[i], arr2[i], arr3[i] <= 2000
'''
import collections
def intersection_of_three_arrays_O_N_method_1(arr1, arr2, arr3):
    map_all_nums_in_dict = collections.defaultdict(int)

    output = []

    for num in arr1:
        map_all_nums_in_dict[num] += 1

    for num in arr2:
        map_all_nums_in_dict[num] += 1     

    for num in arr3:
        map_all_nums_in_dict[num] += 1

    for k, v in map_all_nums_in_dict.items():
        if v == 3:
            output.append(k)

    return output

print(intersection_of_three_arrays_O_N_method_1([1,2,3,4,5], [1,2,5,7,9], [1,3,4,5,8]))                

# using three pointers
def intersection_of_three_arrays_O_N_method_2(arr1, arr2, arr3):

    one = two = three = 0
    output = []
    while one < len(arr1) and two < len(arr2) and three < len(arr3):
        if arr1[one] == arr2[two] == arr3[three]:
            output.append(arr1[one])
            one += 1
            two += 1
            three += 1
        elif arr2[two]  < arr1[one]:
            two += 1
        elif arr3[three]  < arr1[one]:
            three += 1
        else:
            one += 1            

    return output            

print(intersection_of_three_arrays_O_N_method_2([1,2,3,4,5], [1,2,5,7,9], [1,3,4,5,8]))    