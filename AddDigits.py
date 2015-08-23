"""
Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

For example:

Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only one digit, return it.

Follow up:
Could you do it without any loop/recursion in O(1) runtime?
"""
import math
from math import sin, log

class Solution(object):
    def addDigits(self, num):
      if num < 10:
        return num
      newNum = num
      while newNum>=10:
        nextNewNum = 0
        numDigit = int(math.log10(num)) + 1
        everyDigits = []
        for i in range(numDigit-1, 0, -1):
          curDigit = int(newNum/10**i)
          everyDigits.append(curDigit)
          newNum = newNum - curDigit*10**i

        everyDigits.append(newNum)

        for elm in everyDigits:
          nextNewNum += elm
        newNum = nextNewNum

      return newNum


if __name__ == "__main__":
  test = Solution()
  print test.addDigits(19)
  print test.addDigits(20)
  print test.addDigits(37)