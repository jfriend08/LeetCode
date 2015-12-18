'''
Given a collection of numbers, return all possible permutations.

For example,
[1,2,3] have the following permutations:
[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], and [3,2,1].

'''

class Solution(object):
  def permute(self, nums):
    # print 'nums', nums, len(nums)

    if len(nums) == 1:
      return [[nums[0]]]
    if not nums:
      return []

    results = []
    for i in xrange(len(nums)):
      tmpnums = nums[:]
      num = nums[i]
      del tmpnums[i]
      eachresult = [ [num] + eachR for eachR in self.permute(tmpnums)]
      results.extend(eachresult)
    return results

sol = Solution()
final = sol.permute([1,2,3])
print "final ", final