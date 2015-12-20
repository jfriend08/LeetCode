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
    print "nums", nums
    maxidx = len(nums) - 1
    if maxidx == 0:
      return True

    nid = 0
    while nid <= maxidx and not nums[nid] == 0:
      for i in xrange(nid, nid+nums[nid]+1):
        next_id = nid + nums[i]
        if next_id >= maxidx:
          return True
        elif nums[next_id] != 0:
          result = self.canJump(nums[next_id:])
          if result:
            return True
        else:
          continue
    return False

sol = Solution()
print sol.canJump([3,2,1,0,4])
print sol.canJump([2,3,1,1,4])
# print sol.canJump([0])
# print sol.canJump([2,5,0,0])