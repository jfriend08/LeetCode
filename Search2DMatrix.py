'''
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
For example,

Consider the following matrix:

[
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
Given target = 3, return true.
'''

class Solution(object):
  def searchMatrix(self, matrix, target):
    if not matrix:
      return False
    nr, nc = len(matrix), len(matrix[0])

    l_idx, h_idx = 0, nr-1
    decide_r = 0
    while True:
      m_idx = int((l_idx+h_idx)/2)
      if l_idx >= h_idx:
        decide_r = (l_idx if matrix[l_idx][0] <= target else l_idx - 1)
        break
      if matrix[m_idx][0] == target:
        return True
      elif matrix[m_idx][0] > target:
        h_idx = m_idx - 1
      else:
        l_idx = m_idx + 1

    print decide_r
    l_idx, h_idx = 0, nc-1
    while True:
      m_idx = int((l_idx+h_idx)/2)
      if l_idx > h_idx:
        return False
      if matrix[decide_r][m_idx] == target:
        return True
      elif matrix[decide_r][m_idx] > target:
        h_idx = m_idx - 1
      else:
        l_idx = m_idx + 1

arr = [[1,3,5,7],[10,11,16,20],[23,30,34,50]]
arr = [[1,3,5,7]]
sol = Solution()
# print sol.searchMatrix(arr, 10)
# print sol.searchMatrix(arr, 1)
print sol.searchMatrix(arr,5)

