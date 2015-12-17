'''
Given a string array words, find the maximum value of length(word[i]) * length(word[j]) where the two words do not share common letters. You may assume that each word will contain only lower case letters. If no such two words exist, return 0.

Example 1:
Given ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
Return 16
The two words can be "abcw", "xtfn".

Example 2:
Given ["a", "ab", "abc", "d", "cd", "bcd", "abcd"]
Return 4
The two words can be "ab", "cd".

Example 3:
Given ["a", "aa", "aaa", "aaaa"]
Return 0
No such pair of words.
'''
import sys
class Solution(object):

  def getNoInterLetters(self, intersect, word):
    result = []
    for w in word:
      if w not in intersect:
        result.append(w)
    return result

  def maxProduct(self, words):
    maxProduct = -sys.maxint-1
    for i in xrange(0, len(words)-1):
      for j in xrange(i, len(words)):
        word1, word2 = words[i], words[j]
        intersect = set([w for w in word1]) & set([w for w in word2])
        maxProduct = max(maxProduct, len(self.getNoInterLetters(intersect, word1)) * len(self.getNoInterLetters(intersect, word2)))

    return maxProduct



sol = Solution()
print sol.maxProduct(["abcw", "baz", "foo", "bar", "xtfn", "abcdef"])
print sol.maxProduct(["a", "ab", "abc", "d", "cd", "bcd", "abcd"])
print sol.maxProduct(["a", "aa", "aaa", "aaaa"])
