"""
Given an array of integers and an integer k, find out whether there are two distinct indices i and j
in the array such that nums[i] = nums[j] and the difference between i and j is at most k.
"""

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
      if k == 0:
        return False
      for idx0 in range(len(nums)):
        freqMap = {}
        for idx in range(idx0, idx0+k+1):
          if idx >= len(nums):
            break
          try:
            freqMap[nums[idx]] = freqMap[nums[idx]] +1
            return True
          except:
            freqMap[nums[idx]] = 1
      return False