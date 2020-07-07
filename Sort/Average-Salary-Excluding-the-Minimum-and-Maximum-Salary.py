#!/usr/bin/env python3
'''
1491. Average Salary Excluding the Minimum and Maximum Salary
Given an array of unique integers salary where salary[i] is the salary of the employee i.

Return the average salary of employees excluding the minimum and maximum salary.

Example 1:
Input: salary = [4000,3000,1000,2000]
Output: 2500.00000
Explanation: Minimum salary and maximum salary are 1000 and 4000 respectively.
Average salary excluding minimum and maximum salary is (2000+3000)/2= 2500

Example 2:
Input: salary = [1000,2000,3000]
Output: 2000.00000
Explanation: Minimum salary and maximum salary are 1000 and 3000 respectively.
Average salary excluding minimum and maximum salary is (2000)/1= 2000
'''
def Avg_Sal_Excluding_Min_Max(arr):
    arr.sort()

    sum = 0
    for count, sal in enumerate(arr[1:-1], start=1):
        #print(f"count {count} sal: {sal}")
        sum +=  sal

    return sum / count

print(Avg_Sal_Excluding_Min_Max([4000,3000,1000,2000]))     
print(Avg_Sal_Excluding_Min_Max([8000,9000,2000,3000,6000,1000]))     






    