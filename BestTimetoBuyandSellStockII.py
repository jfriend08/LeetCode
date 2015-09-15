'''
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times). However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
'''

class Solution(object):
    def __init__(self):
        self.maxProfitMatrix = None

    def maxProfitHelper(self, prices, i, j):
        if i == j:
          return self.maxProfitMatrix[i][j]
        elif j == i+1 and prices[i] < prices[j]:
          self.maxProfitMatrix[i][j] = prices[j] - prices[i]
          return self.maxProfitMatrix[i][j]
        elif j == i+1 and prices[i] >= prices[j]:
          self.maxProfitMatrix[i][j] = 0
          return self.maxProfitMatrix[i][j]

        for k in range(i,j+1):
          print self.maxProfitMatrix
          tmpVal = self.maxProfitHelper(prices, i, k) + self.maxProfitHelper(prices, k+1, j)
          if tmpVal > self.maxProfitMatrix[i][j]:
            self.maxProfitMatrix[i][j] = tmpVal


    def maxProfit(self, prices):
        if not prices:
          return 0
        tmpMin = -sys.maxint - 1
        self.maxProfitMatrix = [[tmpMin for x in range(len(prices))] for x in range(len(prices))]
        for i in range(len(prices)):
          self.maxProfitMatrix[i][i] = 0
        self.maxProfitHelper(prices, 0, len(prices)-1)
        return self.maxProfitMatrix[0][len(prices)-1]