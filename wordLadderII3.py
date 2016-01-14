from collections import defaultdict
class Solution:
  def findLadders(self, beginWord, endWord, wordlist):
    front, back, leng, forward, result = {}, {}, len(beginWord), True, []

    front[beginWord] = [[beginWord]]
    back[endWord] = [[endWord]]

    wordlist.discard(beginWord)
    if not endWord in wordlist:
      wordlist.add(endWord)

    while len(front) != 0:
      nextSet = {}
      for word in front.keys():
        paths = front[word]
        for i in xrange(leng):
          for c in "abcdefghijklmnopqrstuvwxyz":
            newWord = word[:i] + c + word[i+1:]
            if newWord in wordlist:
              if not newWord in nextSet:
                nextSet[newWord] = []
              if forward:
                nextSet[newWord] += [ path + [newWord] for path in paths]
              else:
                nextSet[newWord] += [ [newWord] + path for path in paths]

      front = nextSet
      common = set(front) & set(back)

      if common:
        if not forward:
          front, back = back, front
        result += [ head + tail[1:] for word in common for head in front[word] for tail in back[word]]
        return result

      if len(front) > len(back):
        front, back, forward = back, front, not forward

      wordlist -= set(front)
    return []



beginWord = "red"
endWord = "tax"
wordList = set(["ted","tex","red","tax","tad","den","rex","pee"])

sol = Solution()
print sol.findLadders(beginWord, endWord, wordList)






