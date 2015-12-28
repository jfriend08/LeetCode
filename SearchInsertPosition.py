'''
Given a sorted array and a target value, return the index if the target is found.
If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Here are few examples.
[1,3,5,6], 5 -> 2
[1,3,5,6], 2 -> 1
[1,3,5,6], 7 -> 4
[1,3,5,6], 0 -> 0
'''

class Solution(object):
  def searchInsert(self, nums, target):
    if target < nums[0]:
      return 0
    if target > nums[-1]:
      return len(nums)

    l_idx, h_idx = 0, len(nums)-1

    while True:
      m_idx = int((l_idx+h_idx)/2)
      if l_idx >= h_idx:
        return l_idx
      elif target > nums[m_idx]:
        l_idx = m_idx + 1
      else:
        h_idx = m_idx

sol = Solution()
print sol.searchInsert([1,3,5,6], 5)
print sol.searchInsert([1,3,5,6], 2)
print sol.searchInsert([1,3,5,6], 4)
print sol.searchInsert([1,3,5,6], 0)

