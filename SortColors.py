'''
Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent,
with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note:
You are not suppose to use the library's sort function for this problem.

Follow up:
A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's,
then 1's and followed by 2's.

Could you come up with an one-pass algorithm using only constant space?
'''

class Solution(object):
  def sortColors(self, nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    rc, wc, bc = 0, 0, 0
    for num in nums:
      if num == 0:
        rc += 1
      elif num == 1:
        wc += 1
      elif num == 2:
        bc += 1

    for i in xrange(len(nums)):
      if i < rc:
        nums[i] = 0
      elif i < rc + wc:
        nums[i] = 1
      else:
        nums[i] = 2

sol = Solution()
arr = [0,1,0,2,0,2,0,2,1,0,2,0,1,2,0,0]
# arr = [1]
print arr
sol.sortColors(arr)
print arr
