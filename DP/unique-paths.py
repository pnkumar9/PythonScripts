#!/usr/bin/env python3
'''
62. Unique Paths
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. 
The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?
Example 1:

Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right
Example 2:

Input: m = 7, n = 3
Output: 28

'''

'''
Everytime it moves right --> column number will be increases 0----n-1
Everytime it moves down --> row number will be increase      0----m-1

There will be total of m-1 (go down)  + n-1 moves (go right) ==> m+n-2

this boils down to choose (n-1) from (m+n-2) which is equivalent to choose (m-1) from (m+n-2)

Decrease-and-conquer method

2D array
array[0][0] is starting point
array[m-1][n-1] is ending point
0 1 ------------n-2 n-1
0
1
2
|
|
|
m-2
m-1--------------[target]

In Python 3.8, there's a new function that calculates n-choose-k directly:
def uniquePaths(self, m: int, n: int) -> int:
    return math.comb(m + n - 2, n - 1)
'''

#Omkar's solution
def uniquePaths(self, m, n):
    #initialize 2D array
        table = [[0 for x in range(n)] for x in range(m)]
        for i in range(m):
            table[i][0] = 1
        for i in range(n):
            table[0][i] = 1

        #above initialization can be replaced with  table = [[1] * n for _ in range(m)]    
        for i in range(1,m):
            for j in range(1,n):
                table[i][j] = table[i-1][j] + table[i][j-1]
        return table[m-1][n-1]


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        d = [[1] * n for _ in range(m)]

        for col in range(1, m):
            for row in range(1, n):
                d[col][row] = d[col - 1][row] + d[col][row - 1]

        return d[m - 1][n - 1]