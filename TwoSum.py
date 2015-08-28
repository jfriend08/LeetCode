'''
Given an array of integers, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2
'''

class Solution(object):
    def twoSum(self, nums, target):
      remainingMap = {}

      for idx in range(len(nums)):
        remainingMap[target-nums[idx]] = idx

      for idx in range(len(nums)):
        try:
          if remainingMap[nums[idx]] != idx:
            idx2 = remainingMap[nums[idx]]
            idx1 = idx

        except:
          continue
      ans = []
      if idx2 > idx1:
        ans.append(idx1+1)
        ans.append(idx2+1)
      else:
        ans.append(idx2+1)
        ans.append(idx1+1)
      return ans