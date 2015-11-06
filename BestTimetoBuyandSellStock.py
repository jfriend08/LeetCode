'''
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.
'''

class Solution(object):
    def maxProfit(self, prices):
        buySellTable = [[None for j in range(len(prices))] for i in range(len(prices))]
        for i in range(len(prices)):
          buySellTable[i][i] = 0

        for buyDay in range(len(prices)-2,-1,-1):
            nextDayDiff = prices[buyDay+1] - prices[buyDay]
            buySellTable[buyDay][buyDay+1] = nextDayDiff
          for sellDay in range(buyDay+2,len(prices)):
            if buySellTable[buyDay+1][sellDay+1]:
              buySellTable[buyDay][sellDay] = buySellTable[buyDay+1][sellDay+1] + nextDayDiff



