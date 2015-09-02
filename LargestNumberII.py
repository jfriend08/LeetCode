'''
Given a list of non negative integers, arrange them such that they form the largest number.

For example, given [3, 30, 34, 5, 9], the largest formed number is 9534330.

Note: The result may be very large, so you need to return a string instead of an integer.

Credits:
Special thanks to @ts for adding this problem and creating all test cases.
'''

class Solution(object):
    def largestNumber(self, nums):
        struct = []
        result = ''
        nums = map(str,nums)

        nums.sort(cmp= lambda x,y: cmp(y+x, x+y))
        return '0' if nums[0]== '0' else ''.join(nums)




if __name__ == "__main__":
    test = Solution()
    print test.largestNumber([3, 30, 34, 5, 9])
    print test.largestNumber([0,0])