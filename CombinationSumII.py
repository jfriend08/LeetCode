'''
Given a set of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.

Note:
All numbers (including target) will be positive integers.
Elements in a combination (a1, a2, ... , ak) must be in non-descending order. (ie, a1 <= a2 <= ... <= ak).
The solution set must not contain duplicate combinations.
For example, given candidate set 2,3,6,7 and target 7,
A solution set is:
[7]
[2, 2, 3]
'''

class Solution(object):
  def combineSumHandler (self, candidates, target):
    result = []

    if not candidates or candidates[0] > target:
      return []
    if candidates[0] == target:
      return [[candidates[0]]]

    withme = self.combineSumHandler(candidates, target-candidates[0])
    result = [ [candidates[0]] + elm for elm in withme ]

    withoutme = self.combineSumHandler(candidates[1:], target)
    result.extend(withoutme)

    return result


  def combinationSum(self, candidates, target):
    return self.combineSumHandler(sorted(set(candidates)), target)


sol = Solution()
print sol.combinationSum([2,3,6,7], 7)
print sol.combinationSum([1, 2], 3)
print sol.combinationSum([1], 2)