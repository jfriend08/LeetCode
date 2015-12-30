'''
According to the Wikipedia's article: "The Game of Life, also known simply as Life,
is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

Given a board with m by n cells, each cell has an initial state live (1) or dead (0).
Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies, as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population..
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
Write a function to compute the next state (after one update) of the board given its current state.

Follow up:
Could you solve it in-place? Remember that the board needs to be updated at the same time: You cannot update some cells first and
then use their updated values toupdate other cells.
In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when
the active area encroaches the border of the array. How would you address these problems?
'''
import copy
class Solution(object):
  def gameOfLife(self, board):
    """
    :type board: List[List[int]]
    :rtype: void Do not return anything, modify board in-place instead.
    """
    nr, nc = len(board), len(board[0])
    nextState = [[-1 for j in xrange(nc)] for i in xrange(nr)]
    for i in xrange(nr):
      for j in xrange(nc):
        c = -board[i][j]
        for i_tmp in xrange(-1, 2, 1):
          for j_tmp in xrange(-1, 2, 1):
            if i-i_tmp < 0 or j-j_tmp < 0:
              continue
            try:
              c += board[i-i_tmp][j-j_tmp]
            except:
              continue
        if board[i][j] == 1 and c < 2:
          nextState[i][j] = 0
        elif board[i][j] == 1 and c <= 3:
          nextState[i][j] = 1
        elif board[i][j] == 1 and c > 3:
          nextState[i][j] = 0
        elif board[i][j] == 0 and c == 3:
          nextState[i][j] = 1
        else:
          nextState[i][j] = 0

    for i in xrange(nr):
      for j in xrange(nc):
        board[i][j] = nextState[i][j]


arr = [[1]]
# print arr
sol = Solution()
sol.gameOfLife(arr)
print arr
