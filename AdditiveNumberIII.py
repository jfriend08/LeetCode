'''
Additive number is a string whose digits can form additive sequence.

A valid additive sequence should contain at least three numbers. Except for the first two numbers, each subsequent number in the sequence must be the sum of the preceding two.

For example:
"112358" is an additive number because the digits can form an additive sequence: 1, 1, 2, 3, 5, 8.

1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
"199100199" is also an additive number, the additive sequence is: 1, 99, 100, 199.
1 + 99 = 100, 99 + 100 = 199
Note: Numbers in the additive sequence cannot have leading zeros, so sequence 1, 2, 03 or 1, 02, 3 is invalid.

Given a string containing only digits '0'-'9', write a function to determine if it's an additive number.

Follow up:
How would you handle overflow for very large input integers?

Credits:
Special thanks to @jeantimex for adding this problem and creating all test cases.
'''

import itertools

class Solution(object):
  def isAdditiveNumber(self, num):
    for i, j in itertools.combinations(range(1,len(num)), 2):
      num1 = int(num[0:i])
      num2 = int(num[i:j])
      if str(num1) != "".join(num[0:i]) or str(num2) != "".join(num[i:j]):
        continue
      while j <= len(num):
        num3 = num1 + num2
        print "(i, j)", (i, j), num1, num2, num3
        idx = num[j-1:].find(str(num3))
        # print "j, idx", j, idx
        if j-1 + idx == j:
          num1, num2 = num2, num3
          j += len(str(num3))
          if j >= len(num):
            return True
        else:
          j += 1
    return False


sol = Solution()
# print sol.isAdditiveNumber("112358")
# print sol.isAdditiveNumber("101")
print sol.isAdditiveNumber("8917")
print sol.isAdditiveNumber("211738")
print sol.isAdditiveNumber("1023")
print sol.isAdditiveNumber("1203")
print sol.isAdditiveNumber("0235813")