'''
121. Best Time to Buy and Sell Stock
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), 
design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
Example 2:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
'''

#Using element comparison
class Solution1(object):
    def maxProfit(self, prices):

        low = float('inf') # set initial low price to be infinite 
        profit = 0 # set profit to be 0 
        for price in prices:
            if price < low:  # detect current price are lower than low
                low = price 
            else:  # detect current price are higher
                profit = max(price-low, profit) # compare the current difference and previous max profit
        return profit

#Dynamic programming
class Solution2(object):
    def maxProfit(self, prices):
    
        fb, fs = float('inf'), 0
        for price in prices:
            fb = min(fb, price) # keep minimal
            fs = max(fs, price-fb) # compute max difference
        return fs