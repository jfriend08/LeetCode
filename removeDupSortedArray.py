'''
Follow up for "Remove Duplicates":
What if duplicates are allowed at most twice?

For example,
Given sorted array nums = [1,1,1,2,2,3],

Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3.
It doesn't matter what you leave beyond the new length.

Subscribe to see which companies asked this question
'''

class Solution(object):
  def removeDuplicates(self, nums):
    if not nums:
      return 0
    mapCount = {}
    maxNum = nums[-1]
    for num in nums:
      try:
        mapCount[num] += 1
      except:
        mapCount[num] = 1

    res = []
    for num in xrange(maxNum+1):
      if num in mapCount:
        res += ( [num] if mapCount[num]==1 else [num, num])
    return len(res)

sol = Solution()
print sol.removeDuplicates([1,1,1,2,2,3])
print sol.removeDuplicates([])
