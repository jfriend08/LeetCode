'''
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?


Above is a 3 x 7 grid. How many possible unique paths are there?
'''

class Solution(object):
  def __init__(self):
    self.lookup = {}

  def dpHelper(self, m, n):
    if m == 1 and n == 1:
      num = 1
    elif (m,n) in self.lookup:
        num = self.lookup[(m,n)]
    elif m == 1:
      num = self.uniquePaths(m,n-1)
    elif n == 1:
      num = self.uniquePaths(m-1,n)
    else:
      num = self.uniquePaths(m-1, n) + self.uniquePaths(m, n-1)

    self.lookup[(m,n)] = num
    return num

  def uniquePaths(self, m, n):
    self.dpHelper(m,n)
    return self.lookup[(m,n)]

sol = Solution()
print sol.uniquePaths(3,5)