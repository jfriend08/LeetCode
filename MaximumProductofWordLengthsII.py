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

  def maxProduct(self, words):
    def convert(c):
      return ord(c) - ord("a")

    def getBits(s):
      return reduce(lambda x,y: x|1<<y, map(convert,s), 0)

    bits, lens = map(getBits, words), map(len, words)

    res = 0
    for i in xrange(len(words)):
      for j in xrange(i, len(words)):
        if not bits[i] & bits[j]:
          res = max(res, lens[i]*lens[j])
    return res



sol = Solution()
print sol.maxProduct(["a", "ab"])
print sol.maxProduct(["a", "ab", "abc", "d", "cd", "bcd", "abcd"])
