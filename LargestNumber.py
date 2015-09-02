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
        for num in nums:
          size = len(str(num))
          digit = int(num/10**(size-1))
          struct.append((digit,num))

        struct = sorted(struct, key = lambda x: (x[0], x[1]), reverse = True)
        for (digit, num) in struct:
          result += str(num)

        return result



if __name__ == "__main__":
    test = Solution()
    print test.largestNumber([3, 30, 34, 5, 9])