'''
Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.

For example:

Given nums = [1, 2, 1, 3, 2, 5], return [3, 5].

Note:
The order of the result is not important. So in the above example, [5, 3] is also correct.
Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?
'''


class Solution(object):
    def singleNumber(self, nums):
        xorResult = 0
        for num in nums:
          xorResult ^= num

        screen = 1
        while not screen & xorResult:
          screen = screen<<1

        numA = 0
        numB = 0
        for num in nums:
          if num & screen:
            numA ^= num
          else:
            numB ^= num
        return [numA, numB]

if __name__ == '__main__':
  test = Solution()
  print test.singleNumber([1,2,1,2,5,3,1,3])