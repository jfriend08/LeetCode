"""
Given an array of integers and an integer k, find out whether there are two distinct indices i and j
in the array such that nums[i] = nums[j] and the difference between i and j is at most k.
"""

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
      if k == 0:
        return False
      freqMap = {}
      for idx in range(0,k+1):
        if idx >= len(nums):
            break
        try:
          freqMap[nums[idx]] = freqMap[nums[idx]] + 1
          return True
        except:
          freqMap[nums[idx]] = 1

      print freqMap

      idx_next = k+1
      while(idx_next<len(nums)):
        idx_last = idx_next - k-1
        print "idx_next: %s, idx_last: %s"%(idx_next, idx_last)
        if nums[idx_next] == nums[idx_last]:
          if freqMap[nums[idx_last]] > 1:
            freqMap[nums[idx_last]]-=1
            return True
        else:
          try:
            freqMap[nums[idx_next]] += 1
            return True
          except:
            freqMap[nums[idx_next]]=1
          if freqMap[nums[idx_last]] > 1:
            freqMap[nums[idx_last]] -= 1
          else:
            freqMap.pop(nums[idx_last])

        idx_next += 1
        print freqMap

      return False


if __name__ == "__main__":
    test = Solution()
    mylist = [1,2,3,4,5,6,7,8,9,9]
    print test.containsNearbyDuplicate(mylist,3)



