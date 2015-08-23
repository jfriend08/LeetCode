"""
Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

For example:

Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only one digit, return it.

Follow up:
Could you do it without any loop/recursion in O(1) runtime?
"""
import math

class Solution(object):
    def addDigits(self, num):
      if num<10:
        return num

      newNum = num

      # for num>10, process it
      while newNum>=10:
        digitList = []
        numDigit = int(math.log10(newNum))+1
        for power in range(numDigit-1, 0, -1):
          eachDigit = int(newNum/10**power)
          digitList.append(eachDigit)
          newNum = newNum - eachDigit*10**power

        digitList.append(newNum)

        digitSum = 0
        for elm in digitList:
          digitSum = digitSum+ elm

        newNum = digitSum

      return newNum

if __name__ == "__main__":
  test = Solution()
  print test.addDigits(19)
  print test.addDigits(20)
  print test.addDigits(37)


