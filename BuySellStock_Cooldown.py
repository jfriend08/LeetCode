'''
Best Time to Buy and Sell Stock with Cooldown My Submissions Question
Total Accepted: 2675 Total Submissions: 7981 Difficulty: Medium
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times) with the following restrictions:

You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)
Example:

prices = [1, 2, 3, 0, 2]
maxProfit = 3
transactions = [buy, sell, cooldown, buy, sell]
'''
import sys

class Solution(object):
  def maxSellAt(self, j, prices):
    maxprofit = -sys.maxint -1
    for price_idx in xrange(j):
      tmp_profit = prices[j] - prices[price_idx]
      if tmp_profit > maxprofit:
        maxprofit = tmp_profit
    return maxprofit

  def maxProfit(self, prices):
    maxprofit = -sys.maxint -1

    if len(prices) == 2:
      diff = prices[1]-prices[0]
      return (diff if diff >0 else 0)

    for i in xrange(1, len(prices)):
      tmp_profit = self.maxSellAt(i, prices) + self.maxProfit(prices[i+2:])
      if maxprofit < tmp_profit:
        maxprofit = tmp_profit

    return maxprofit

sol = Solution()
print sol.maxProfit([1, 2, 3, 0, 2])
