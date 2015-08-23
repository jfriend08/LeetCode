"""
Given a sorted integer array without duplicates, return the summary of its ranges.

For example, given [0,1,2,4,5,7], return ["0->2","4->5","7"].

Credits:
Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.
"""


class Solution(object):
    def summaryRanges(self, nums):
      beginning = None
      rangeArray = []
      isContinue = False

      if len(nums)==1:
        rangeArray.append(str(nums[0]))
        return rangeArray
      elif len(nums)==0:
        return rangeArray

      for i in range(len(nums)):
        if beginning == None:
          beginning = nums[i]
        elif nums[i] - nums[i-1] != 1:
          if nums[i-1] != beginning:
            rangeArray.append(str(beginning) + "->" + str(nums[i-1]))
            # rangeArray.append("%s->%s"%(beginning, nums[i-1]))
          else:
            rangeArray.append(str(nums[i-1]))
          beginning = nums[i]

      if nums[-1] != beginning:
        rangeArray.append(str(beginning) + "->" + str(nums[-1]))
      else:
        rangeArray.append(str(nums[-1]))

      return rangeArray