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
  def __init__ (self):
    self.target = None

  def combineSumHandler (self, candidates, sumlist):
    loc_candidates = candidates[:]
    loc_sumlist = sumlist[:]
    results = []
    remain = self.target - sum(loc_sumlist)

    for elm in sumlist:
      mod = remain % elm
      if mod == 0:
        for i in xrange(remain/elm):
          loc_sumlist.append(elm)
        results.append(sorted(loc_sumlist))
        loc_sumlist = sumlist[:]
      else:
        continue

    if len(candidates) != 0 and remain == candidates[0]:
      loc_sumlist.append(candidates[0])
      results.append(loc_sumlist)
      return results

    if sum(sumlist) == self.target:
      results.append(sumlist)
      return results

    if len(candidates) == 0:
      return results

    loc_sumlist.append(loc_candidates[0])

    if sum(loc_sumlist) <= self.target:
      hasme = self.combineSumHandler(candidates[1:], loc_sumlist)
      results.extend(hasme)

    nome = self.combineSumHandler(candidates[1:], sumlist)
    results.extend(nome)

    return map(list, set(map(tuple, results)))

  def combinationSum(self, candidates, target):
    self.target = target
    candidates = sorted(list(set(candidates)))
    return self.combineSumHandler(candidates, [])

sol = Solution()
print sol.combinationSum([2,3,6,7], 7)
print sol.combinationSum([1], 2)
print sol.combinationSum([1, 3, 4, 2], 4)
print sol.combinationSum([1, 2], 3)


