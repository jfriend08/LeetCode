'''
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters.
No two characters may map to the same character but a character may map to itself.

For example,
Given "egg", "add", return true.

Given "foo", "bar", return false.

Given "paper", "title", return true.

Note:
You may assume both s and t have the same length.
'''


class Solution(object):
    def isIsomorphic(self, s, t):
      translateDict = {}
      beingUsedDict = {}
      for idx in range(len(s)):
        try:
          isTheSame = translateDict[s[idx]]==t[idx]
          if not isTheSame:
            return False
        except:
          if t[idx] in beingUsedDict:
            return False
          translateDict[s[idx]] = t[idx]
          beingUsedDict[t[idx]] = True

      return True
