'''
Given n balloons, indexed from 0 to n-1. Each balloon is painted with a number on it represented by array nums.
You are asked to burst all the balloons. If the you burst balloon i you will get nums[left] * nums[i] * nums[right] coins.
Here left and right are adjacent indices of i. After the burst, the left and right then becomes adjacent.

Find the maximum coins you can collect by bursting the balloons wisely.

Note:
(1) You may imagine nums[-1] = nums[n] = 1. They are not real therefore you can not burst them.
(2) 0 <= n <= 500, 0 <= nums[i] <= 100

Example:

Given [3, 1, 5, 8]

Return 167

    nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
   coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167

'''

import sys


class Solution(object):
  def __init__(self):
    self.lookup = {}
  def maxCoins(self, nums):
    if tuple(nums) in self.lookup:
      return self.lookup[tuple(nums)]

    if len(nums) == 1:
      val = None
      if tuple(nums) in self.lookup:
        val = self.lookup[tuple(nums)]
      else:
        self.lookup[tuple(nums)] = nums[0]
        val = nums[0]
      return nums[0]
    else:
      maxVal = -sys.maxint - 1
      for i in xrange(len(nums)):
        newlist = nums[:]
        del newlist[i]
        if i == 0:
          val = 1 * nums[i] * nums[i+1] + self.maxCoins(newlist)
        elif i == len(nums)-1:
          val = nums[i-1] * nums[i] * 1 + self.maxCoins(newlist)
        else:
          val = nums[i-1] * nums[i] * nums[i+1] + self.maxCoins(newlist)
        if maxVal < val:
          maxVal = val
      self.lookup[tuple(nums)] = maxVal
      return maxVal


sol = Solution()
print sol.maxCoins([3,1,5,8])
sol = Solution()
print sol.maxCoins([8,2,6,8,9,8,1,4,1,5,3,0,7,7,0,4,2])






