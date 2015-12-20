'''
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

For example:
A = [2,3,1,1,4], return true.

A = [3,2,1,0,4], return false.
'''

class Solution(object):
  def canJump(self, nums):
    reach = 0
    for i in xrange(0, len(nums)):
      if i > reach:
        break
      reach = max(reach, i+nums[i])
    return reach >= len(nums) - 1

sol = Solution()
print sol.canJump([3,2,1,0,4])
print sol.canJump([2,3,1,1,4])
print sol.canJump([0])
print sol.canJump([2,5,0,0])
