'''
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.
'''

class Solution(object):
  def maxProfit(self, prices):
    if len(prices) <= 1:
      return 0
    buy, sell, prebuy, presell = -prices[0], 0, 0, 0
    for price in prices:
      prebuy = buy
      buy = max(-1*price, prebuy)
      presell = sell
      sell = max(prebuy+price, presell)
    return sell


sol = Solution()
print sol.maxProfit([3,4,5,1,10,20])