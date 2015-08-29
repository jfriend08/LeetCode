'''
Given an array of n integers where n > 1, nums, return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Solve it without division and in O(n).

For example, given [1,2,3,4], return [24,12,8,6].

Follow up:
Could you solve it with constant space complexity? (Note: The output array does not count as extra space for the purpose of space complexity analysis.)
'''

class Solution(object):
    def productExceptSelf(self, nums):
        size = len(nums)
        right_Product = [1]*size
        left_Product = [1]*size
        result = [1]*size

        tmp_product = 1
        for idx in range(len(nums)-2,-1,-1):
          tmp_product = tmp_product*nums[idx+1]
          right_Product[idx] = tmp_product

        tmp_product = 1
        for idx in range(1,len(nums)):
          tmp_product = tmp_product*nums[idx-1]
          left_Product[idx] = tmp_product

        for idx in range(len(left_Product)):
          result[idx] = right_Product[idx] * left_Product[idx]
        return result

