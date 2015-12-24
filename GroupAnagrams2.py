'''
Given an array of strings, group anagrams together.

For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"],
Return:

[
  ["ate", "eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:
For the return value, each inner list's elements must follow the lexicographic order.
All inputs will be in lower-case.
'''

class Solution(object):
  def getDict(self, mystr):
    res = {}
    for c in mystr:
      try:
        res[c] += 1
      except:
        res[c] = 1
    return res

  def groupAnagrams(self, strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    mydict = {}
    res = []
    for eachstr in strs:
      myT = tuple(sorted(eachstr))
      if myT in mydict:
        idx = mydict[myT]
        res[idx] += [eachstr]
      else:
        mydict[myT] = len(res)
        res += [[eachstr]]
    return map(sorted, res)
sol = Solution()
print sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
print sol.groupAnagrams([])







