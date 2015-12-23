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
    i = 0
    for num in nums:
      if i < 2 or nums[i-2] < num:
        nums[i] = num
        i += 1
    # print nums, i
    return i

sol = Solution()
sol.removeDuplicates([1,1,1,2,2,3])
sol.removeDuplicates([])
