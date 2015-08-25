'''
Write a program to check whether a given number is an ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. For example, 6, 8 are ugly while 14 is not ugly since it includes another prime factor 7.

Note that 1 is typically treated as an ugly number.

Credits:
Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.
'''


class Solution(object):
    def getPower(self,num,base):
      remain = num
      powerCount = 0
      while remain % base == 0:
        powerCount += 1
        remain = remain/base
      return (powerCount, remain)


    def isUgly(self, num):
      if num==1 or num==2 or num==3 or num==5:
        return True
      elif num ==0:
        return False
      (power2, remain) = self.getPower(num, 2)
      (power3, remain) = self.getPower(remain, 3)
      (power5, remain) = self.getPower(remain, 5)

      if remain != 1:
        return False
      else:
        return True

if __name__ == "__main__":
  test = Solution()
  print test.isUgly(8)
  print test.isUgly(21)