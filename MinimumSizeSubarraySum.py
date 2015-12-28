'''
Given an array of n positive integers and a positive integer s, find the minimal length of a subarray of which the sum >= s.
If there isn't one, return 0 instead.

For example, given the array [2,3,1,2,4,3] and s = 7,
the subarray [4,3] has the minimal length under the problem constraint.


More practice:
If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(nlogn).
'''

class Solution(object):
  def minSubArrayLen(self, s, nums):
    if not nums:
      return 0
    remainM = {}
    for num in nums:
      if not remainM.keys():
        remainM[s-num] = [num]
        continue

      for remain in sorted(remainM.keys(), reverse=True):
        newRemain = remain - num
        if newRemain >= 0:
          try:
            remainM[newRemain] = (remainM[newRemain] if len(remainM[newRemain]) <= len(remainM[remain]) + 1 else remainM[remain] + [num])
          except:
            remainM[newRemain] = remainM[remain] + [num]
        else:
          break
      if s - num >= 0 and not s - num in remainM:
        remainM[s-num] = [num]
    try:
      return len(remainM[0])
    except:
      return 0

sol = Solution()
print sol.minSubArrayLen(7, [2,3,1,2,4,3])

print sol.minSubArrayLen(100, [2,3,1,2,4,3])
