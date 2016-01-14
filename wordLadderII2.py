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

from collections import defaultdict
class Solution(object):
  def findLadders(self, beginWord, endWord, wordlist):
    front, end = defaultdict(list), defaultdict(list)

    front[beginWord] += [[beginWord]]
    end[endWord] += [[endWord]]

    wordlist.discard(beginWord)
    if not endWord in wordlist:
      wordlist.add(endWord)

    forward, result = True, []
    while front:
      nextSet = defaultdict(list)
      for word, paths in front.items():
        for i in xrange(len(word)):
          for c in "abcdefghijklmnopqrstuvwxyz":
            newWord = word[:i] + c + word[i+1:]
            if newWord in wordlist:
              if forward:
                nextSet[newWord] += [ path + [newWord] for path in paths]
              else:
                nextSet[newWord] += [ [newWord] + path for path in paths]

      front = nextSet
      common = set(front) & set(end)

      print "front:", front, "end:", end, common, wordlist
      if common:
        if not forward:
          front, end = end, front
        result += [ head + tail[1:] for word in common for head in front[word] for tail in end[word]]
        return result

      if len(front) > len(end):
        fron, end, forward = end, front, not forward

      wordlist -= set(front)

    return []


beginWord = "hit"
endWord = "cog"
wordList = set(["hot","dot","dog","lot","log"])

sol = Solution()
print sol.findLadders(beginWord, endWord, wordList)

