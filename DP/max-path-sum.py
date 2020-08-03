#!/usr/bin/env python3
'''
'''

'''
Note in Python 2D arrays
Input = ([[1, 2], [3, 4], [5, 6]])
numrows = len(input)    # 3 rows in your example
numcols = len(input[0]) # 2 columns in your example
'''
# O(m*n) space
def minPathSum(self, grid):
    if not grid:
        return 
    r, c = len(grid), len(grid[0])
    dp = [[0 for _ in range(c)] for _ in range(r)]
    dp[0][0] = grid[0][0]
    for i in range(1, r):
        dp[i][0] = dp[i-1][0] + grid[i][0]
    for i in range(1, c):
        dp[0][i] = dp[0][i-1] + grid[0][i]
    for i in range(1, len(grid)):
        for j in range(1, len(grid[0])):
            #row-1,col ==> cell above the current (row, col)
            #row,col-1 ==> cell left of the current (row, col)
            #i = row
            #j = column
            dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
    return dp[-1][-1]


# O(m*n) space
def maxPathSum(self, grid):
    if not grid:
        return 
    r, c = len(grid), len(grid[0])
    dp = [[0 for _ in range(c)] for _ in range(r)]
    dp[0][0] = grid[0][0]
    for i in range(1, r):
        dp[i][0] = dp[i-1][0] + grid[i][0]
    for i in range(1, c):
        dp[0][i] = dp[0][i-1] + grid[0][i]
    for i in range(1, len(grid)):
        for j in range(1, len(grid[0])):
            dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + grid[i][j]
    return dp[-1][-1]