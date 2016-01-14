'''
Word Ladder II

Given two words (beginWord and endWord), and a dictionary's word list, find all shortest transformation sequence(s) from beginWord to endWord, such that:

Only one letter can be changed at a time
Each intermediate word must exist in the word list
For example,

Given:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]
Return
  [
    ["hit","hot","dot","dog","cog"],
    ["hit","hot","lot","log","cog"]
  ]
Note:
All words have the same length.
All words contain only lowercase alphabetic characters.
'''

class Solution(object):
  def isOneLetterDiffer(self, w1, w2):
    if len(w1) != len(w2):
      return False

    diffCount = 0
    for i in xrange(len(w1)):
      if w1[i] != w2[i]:
        diffCount += 1
    return diffCount == 1

  def findLaddersUtil(self, beginWord, endWord, res, collect, preIdx, letterMap, wordMap):
    if self.isOneLetterDiffer(beginWord, endWord):
      res += [collect+[endWord]]
      return
    elif len(preIdx.keys()) == len(endWord):
      return

    for i in xrange(len(beginWord)):
      if i in preIdx:
        continue
      else:
        for c in letterMap[i]:
          wordA = list(beginWord)
          wordA[i] = c
          newW = "".join(wordA)
          if newW in wordMap:
            copyPreIdx = preIdx.copy()
            copyPreIdx[i] = True
            self.findLaddersUtil(newW, endWord, res, collect+[newW], copyPreIdx, letterMap, wordMap)
    return


  def makeDict(self, wordList):
    letterMap = {}
    for i in xrange(len(wordList)):
      word = list(wordList)[i]
      for i in xrange(len(word)):
        if not i in letterMap:
          letterMap[i] = [word[i]]
        else:
          letterMap[i] += [word[i]]
    for key in letterMap.keys():
      letterMap[key] = set(letterMap[key])
    return letterMap, wordList

  def findLadders(self, beginWord, endWord, wordlist):
    letterMap, wordMap = self.makeDict(wordlist)
    res = []
    self.findLaddersUtil(beginWord, endWord, res, [beginWord], {}, letterMap, wordMap)
    return res

beginWord = "hit"
endWord = "cog"
wordList = set(["hot","dot","dog","lot","log"])

sol = Solution()
print sol.findLadders(beginWord, endWord, wordList)
