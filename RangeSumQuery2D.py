'''
Given a 2D matrix matrix, find the sum of the elements inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).

Range Sum Query 2D
The above rectangle (with the red border) is defined by (row1, col1) = (2, 1) and (row2, col2) = (4, 3), which contains sum = 8.

Example:
Given matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]

sumRegion(2, 1, 4, 3) -> 8
sumRegion(1, 1, 2, 2) -> 11
sumRegion(1, 2, 2, 4) -> 12
Note:
You may assume that the matrix does not change.
There are many calls to sumRegion function.
You may assume that row1 <= row2 and col1 <= col2.
'''



class NumMatrix(object):
  def __init__(self, matrix):
    if matrix == []:
      return
    self.orig = matrix
    self.matrix = [[None for j in xrange(len(matrix[0]))] for i in xrange(len(matrix))]
    self.dimX, self.dimY = len(matrix), len(matrix[0])
    for i in xrange(self.dimX-1,-1, -1):
      for j in xrange(self.dimY-1, -1, -1):
        if i == self.dimX - 1 and j == self.dimY - 1:
          self.matrix[i][j] = matrix[i][j]
        elif i == self.dimX - 1:
          self.matrix[i][j] = matrix[i][j] + self.matrix[i][j+1]
        elif j == self.dimY - 1:
          self.matrix[i][j] = matrix[i][j] + self.matrix[i+1][j]
        else:
          self.matrix[i][j] = matrix[i][j] + self.matrix[i+1][j] + self.matrix[i][j+1] - self.matrix[i+1][j+1]

  def sumRegion(self, row1, col1, row2, col2):
    result = self.matrix[row1][col1]

    if row1 == self.dimX-1 and col1 == self.dimY-1:
      return self.matrix[row1][col1]

    if col2 < self.dimY-1:
      result -= self.matrix[row1][col2+1]
    if row2 < self.dimX-1:
      result -= self.matrix[row2+1][col1]
    if col2 < self.dimY-1 and row2 < self.dimX-1:
      result += self.matrix[row2+1][col2+1]
    return result


matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]
numMatrix = NumMatrix(matrix)
print numMatrix.sumRegion(2, 1, 4, 3)
print numMatrix.sumRegion(0, 1, 2, 3)
print numMatrix.sumRegion(1, 2, 3, 3)

# matrix = [[-1]]
# numMatrix = NumMatrix(matrix)
# print numMatrix.sumRegion(0,0,0,0)

# matrix = [[4,5]]
# numMatrix = NumMatrix(matrix)
# print numMatrix.sumRegion(0,0,0,0)
# print numMatrix.sumRegion(0,0,0,1)
# print numMatrix.sumRegion(0,1,0,1)