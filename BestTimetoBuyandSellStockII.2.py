'''
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times). However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
'''

class Solution(object):
    def maxProfit(self, prices):
      if len(prices)<2:
        return 0
      delta = []
      result = 0
      for i in range(1,len(prices)):
        delta.append(prices[i]-prices[i-1])

      for perDelta in delta:
        if perDelta > 0:
          result += perDelta
      return result
