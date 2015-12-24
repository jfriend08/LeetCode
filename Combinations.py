'''
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

For example,
If n = 4 and k = 2, a solution is:

[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
Subscribe to see which companies asked this question
'''
class Solution(object):
  def helper(self, k, allN):
    res = []
    if k == 1:
      return [[num] for num in allN]
    else:
      for i in xrange(len(allN)):
        print allN[i]
        res += [ [allN[i]] + elm for elm in self.helper(k-1, allN[i+1:])]
    return res

  def combine(self, n, k):
    allN = [ i+1 for i in xrange(n)]
    return self.helper(k, allN)

sol = Solution()
print sol.combine(4,2)
