'''
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times). However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
'''

class Solution(object):
    def __init__(self):
        self.maxProfitMatrix = None

    def maxProfitHelper(self, prices, i, j):
        for k in range(i,j):
          tmpVal = self.maxProfitHelper(prices[i:k]) + self.maxProfitHelper(prices[k:j])



    def maxProfit(self, prices):
        tmpMin = -sys.maxint - 1
        self.maxProfitMatrix = [[tmpMin for x in range(len(prices))] for x in range(len(prices))]
        self.maxProfitHelper(prices, 0, len(prices)-1)