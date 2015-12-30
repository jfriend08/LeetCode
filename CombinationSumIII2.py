'''
Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used
and each combination should be a unique set of numbers.

Ensure that numbers within the set are sorted in ascending order.


Example 1:

Input: k = 3, n = 7

Output:

[[1,2,4]]

Example 2:

Input: k = 3, n = 9

Output:

[[1,2,6], [1,3,5], [2,3,4]]
'''

class Solution(object):
  def findResHelper(self, k, n, cand):
    print k, n, cand
    if n == 0 and k == 0:
      return [[]]
    if n != 0 and k == 0 or n < cand[0]:
      return

    res = []
    try:
      withme = [[cand[0]] + elm for elm in self.findResHelper(k-1, n-cand[0], cand[1:])]
      res += withme
    except:
      pass
    try:
      withoutme = self.findResHelper(k, n, cand[1:])
      res += withoutme
    except:
      pass

    return res


  def combinationSum3(self, k, n):
    if n < ((1 + k)*k)/2 or n > ((9+9-k+1)*k)/2:
      return []
    cand = [ i+1 for i in xrange(9)]
    return self.findResHelper(k, n, cand)


sol = Solution()
# print sol.combinationSum3(3,9)
# print sol.combinationSum3(4,24)
# print sol.combinationSum3(2,6)
print sol.combinationSum3(9,45)
