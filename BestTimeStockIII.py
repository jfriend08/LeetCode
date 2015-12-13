'''
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
'''


class Solution(object):
  def maxProfit(self, prices):
    if len(prices) < 2:
      return 0

    buy1, buy2, sell1, sell2 = -prices[0], 0, 0, 0
    prebuy1, prebuy2, presell1, presell2 = 0, 0, 0, 0

    if len(prices) < 2:
      return 0
    for price in prices:
      prebuy1 = buy1
      buy1 = max(-price, prebuy1)
      presell1 = sell1
      sell1 = max(prebuy1 + price, presell1)

      prebuy2 = buy2
      buy2 = max(sell1 - price, buy1)
      sell2 = max(prebuy2 + price, sell2)

    print (sell1, sell2)
    return max(sell1, sell2)

sol = Solution()
print "[1,4,2,7]", sol.maxProfit([1,4,2,7])

print "[1,2,4,7]", sol.maxProfit([1,2,4,7])

print "[1,2,4]", sol.maxProfit([1,2,4])

print "[2,1]", sol.maxProfit([2,1])
print "[3,4,10,1,10,20,1,5]", sol.maxProfit([3,4,10,1,10,20,1,5])
print "[1,0,0,10,1,0,0,9,1,0,0,11,0,0,5]", sol.maxProfit([1,0,0,10,1,0,0,9,1,0,0,11,0,0,5])


