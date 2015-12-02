'''
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].

Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.
'''

class Solution(object):
    def moveZeroes(self, nums):
        zeros = []
        zeroCount = 0
        for elm in nums:
          if elm == 0:
            zeros.append(0)
            zeroCount += 1

        nums.extend(zeros)

        while zeroCount>0:
          for idx in xrange(len(nums)):
            if nums[idx] ==0:
              nums.pop(idx)
              zeroCount -= 1
              break
