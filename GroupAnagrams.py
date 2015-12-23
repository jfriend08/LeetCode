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
    dictArr = []
    res = []
    for eachstr in strs:
      if not dictArr:
        dictArr.append(self.getDict(eachstr))
        res.append([eachstr])
      else:
        thisDict = self.getDict(eachstr)
        hasMatch = False
        for dictI in xrange(len(dictArr)):
          eachdict = dictArr[dictI]
          if cmp(thisDict, eachdict) == 0:
            res[dictI] += [eachstr]
            hasMatch = True
            break
        if not hasMatch:
          dictArr.append(thisDict)
          res.append([eachstr])
    return map(sorted, res)

sol = Solution()
print sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
print sol.groupAnagrams([])







