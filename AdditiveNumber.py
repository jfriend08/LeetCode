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


class Solution(object):
  def isAdditiveNumber(self, num):
    for num1_start in xrange(len(num)):
      i = 2
      num1 = int(num[num1_start:num1_start+i])
      for num2_start in xrange(num1_start+i, len(num)):
        j = 2
        if num2_start+j >= len(num):
          break
        num2 = int(num[num2_start:num2_start+j])
        sumNum = str(num1 + num2)
        findResult = num.find(sumNum, num2_start+j)
        if findResult == num2_start+j:
          num1_start = findResult
        j += 1
      i += 1
