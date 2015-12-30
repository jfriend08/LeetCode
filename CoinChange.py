'''
You are given coins of different denominations and a total amount of money amount.
Write a function to compute the fewest number of coins that you need to make up that amount.
If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:
coins = [1, 2, 5], amount = 11
return 3 (11 = 5 + 5 + 1)

Example 2:
coins = [2], amount = 3
return -1.

Note:
You may assume that you have an infinite number of each kind of coin.
'''
import sys
class Solution(object):
  def coinChange(self, coins, amount):
    """
    :type coins: List[int]
    :type amount: int
    :rtype: int
    """
    coins = sorted(coins)

    if amount == 0:
      return 0

    if coins[0] > amount or not coins:
      return -1
    INF = 0x7ffffffe
    # res = [INF] * (amount+1)
    res = [INF] * (amount+1)
    res[0] = 0
    for num in xrange(0, amount+1):
      for c in coins:
        if num + c <= amount:
          res[num+c] = min(res[num+c], res[num] + 1)
        else:
          break
    return (res[num] if res[num] != INF else -1)
    # res = {}
    # res[0] = 0
    # INF = 0x7ffffffe
    # for num in xrange(0, amount+1):
    #   for c in coins:
    #     if num < c:
    #       break
    #     try:
    #       res[num] = min(res[num], res[num-c] + 1)
    #     except:
    #       res[num] = (INF if num%c != 0 else int(num/c) )
    # print res
    # return (res[amount] if res[amount] != INF else -1)

sol = Solution()
print sol.coinChange([1,2,5], 11)
print sol.coinChange([2], 3)
print sol.coinChange([2], 1)
print sol.coinChange([112,149,215,496,482,436,144,397,500,189], 8480)
print sol.coinChange([368,305,204,88,148,423,296,125,346], 7163)
print sol.coinChange([77,82,84,80,398,286,40,136,162],9794)