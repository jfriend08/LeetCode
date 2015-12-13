'''
Given a string which contains only lowercase letters, remove duplicate letters so that every letter appear once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.

Example:
Given "bcabc"
Return "abc"

Given "cbacdcbc"
Return "acdb"

Credits:
Special thanks to @peisi for adding this problem and creating all test cases.
'''

import sys
import itertools

class Solution(object):
  def __init__(self):
    self.allLetters = {}
    self.score = {}
    letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    for i in xrange(len(letters)):
      self.score[letters[i]] = i

  def initLetterScore(self):
    pass

  def bestScore(self, letters, keys):
    bestScore = sys.maxint

    if len(letters) == 0 and len(keys) != 0:
      return bestScore
    elif len(keys) <= 0:
      return 0

    letters_next = []
    keys_next = keys[:]
    delIdx = keys_next.index(letters[0])
    keys_next.pop(delIdx)

    for elm in letters:
      if elm == letters[0]:
        continue
      else:
        letters_next.append(elm)

    return min(self.bestScore(letters_next[1:], keys), self.score[letters[0]] + self.bestScore(letters_next, keys_next) )



  def removeDuplicateLetters(self, s):
    for char in s:
      self.allLetters[char] = True
    score = self.bestScore(s, self.allLetters.keys())
    allList = itertools.permutations(self.allLetters.keys(), len(self.allLetters.keys()))
    for elm in allList:
      if sum(map(lambda x: self.score[x], elm)) == score:
        return elm

sol = Solution();
print sol.removeDuplicateLetters("bcabc")

