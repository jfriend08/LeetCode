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
    maxidx = len(nums)-1

    if nums[0] >= maxidx:
      return True

    curIdx = 0
    for i in xrange(curIdx+1, curIdx+nums[curIdx]+1):
      nextIdx = curIdx + i
      result = False
      if nums[nextIdx] != 0:
        result = self.canJump(nums[nextIdx:])
      if result:
        return True
    return False

sol = Solution()
print sol.canJump([3,2,1,0,4])
print sol.canJump([2,3,1,1,4])
print sol.canJump([0])
print sol.canJump([2,5,0,0])