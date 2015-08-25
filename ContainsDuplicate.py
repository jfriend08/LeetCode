'''
Given an array of integers, find if the array contains any duplicates.
Your function should return true if any value appears at least twice in the array,
and it should return false if every element is distinct.
'''

class Solution(object):
    def containsDuplicate(self, nums):
        dupDict = {}
        for idx in range(len(nums)):
          try:
            dupDict[nums[idx]] += 1
            return True
          except:
            dupDict[nums[idx]] = 1
        return False