"""
Given an integer, write a function to determine if it is a power of two.

Credits:
Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.
"""
import math
class Solution(object):
    def isPowerOfTwo(self, n):

        if n == 1:
          return True
        elif n <= 0:
          return False

        power = int(math.log(n,2))
        remaining = n - 2**power
        print remaining
        if remaining == 0:
          return True
        return False


if __name__ == "__main__":
  test = Solution()
  print test.isPowerOfTwo(536870912)