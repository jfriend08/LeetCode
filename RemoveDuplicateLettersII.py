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
  def removeDuplicateLetters(self, s):
    for char in sorted(set(s)):
      remain = s[s.index(char):]
      if set(remain) == set(s):
        return char + self.removeDuplicateLetters(remain.replace(char,''))
    return ''


sol = Solution()
print sol.removeDuplicateLetters("cbacdcbc")
print sol.removeDuplicateLetters("bcabc")