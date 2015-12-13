'''
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times).
However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

Subscribe to see which companies asked this question
'''


class Solution(object):
  def maxProfit(self, prices):
    if len(prices) <= 1:
      return 0
    buy, sell, prebuy, presell = -prices[0], 0, 0, 0
    for price in prices:
      prebuy = buy
      presell = sell
      buy = max(presell - price, prebuy)
      sell = max(prebuy + price, presell)
    return sell

sol = Solution()
print sol.maxProfit([3,4,10,1,10,20])
print sol.maxProfit([2,1,2,0,1])