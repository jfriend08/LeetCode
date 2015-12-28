'''
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.

Did you use extra space?
A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?

Subscribe to see which companies asked this question
'''

class Solution(object):
  def setZeroes(self, matrix):
    """
    :type matrix: List[List[int]]
    :rtype: void Do not return anything, modify matrix in-place instead.
    """
    nrow, ncol = len(matrix), len(matrix[0])
    col
    for i in nrow:
      for j in ncol: