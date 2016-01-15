'''
Given a positive integer n, find the least number of perfect square numbers
(for example, 1, 4, 9, 16, ...) which sum to n.

For example, given n = 12, return 3 because 12 = 4 + 4 + 4; given n = 13, return 2 because 13 = 4 + 9.

Credits:
Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.
'''

import math
class Solution(object):
  def numSquares(self, n):
    maxBase = int(n**0.5)
    psns = [num **2 for num in xrange(1, maxBase+1)]
    res = [None] * n

    for num in psns:
      for i in xrange(len(res)):
        if (i+1)%num == 0:
          res[i] = (i+1)/num
        elif num < i+1:
          res[i] = min(res[i], res[i-num]+1)
    return res[-1]


sol = Solution()
print sol.numSquares(13)
print sol.numSquares(12)

print sol.numSquares(6175)