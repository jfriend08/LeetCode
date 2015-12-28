'''
Given an array of n positive integers and a positive integer s, find the minimal length of a subarray of which the sum >= s.
If there isn't one, return 0 instead.

For example, given the array [2,3,1,2,4,3] and s = 7,
the subarray [4,3] has the minimal length under the problem constraint.


More practice:
If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(nlogn).
'''

import sys
class Solution(object):
  def minSubArrayLen(self, s, nums):
    mysum, i, j, minL = 0, 0, 0, sys.maxint
    while j < len(nums):
      while mysum < s and j < len(nums):
        mysum += nums[j]
        j += 1
      if mysum >= s:
        while mysum >= s and i < j:
          mysum -= nums[i]
          i += 1
        minL = min(minL, j-i+1)

    return (minL if minL != sys.maxint else 0)


sol = Solution()
print sol.minSubArrayLen(7, [2,3,1,2,4,3])
print sol.minSubArrayLen(100, [2,3,1,2,4,3])
print sol.minSubArrayLen(5, [2,3,1,1,1,1,1])