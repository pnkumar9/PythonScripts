
'''
322. Coin Change
You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:

Input: coins = [1, 2, 5], amount = 11
Output: 3 
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Note:
You may assume that you have an infinite number of each kind of coin.
coinchange.png
'''

'''
Remember this formula
In the coin change problem, if coins = [1,2], then the recurrence equation for the optimal solution would be:

f(a) = min(f(a-1),f(a-2)) + 1
''' 

#****** Please see coin change II problem after this. filename: numberOfWaysToMakeChange.py
#***************************************************

def minNumberOfCoinsForChange(n, denoms):
    # build dp table
	dp = [float("inf")] * (n+1)
	
	dp[0] = 0
	
	for denom in denoms:
		for amount in range(len(dp)):
			if denom <= amount:
				dp[amount] = min(dp[amount], 1 + dp[amount-denom])
				
	return dp[n] if dp[n] != float("inf") else -1	        