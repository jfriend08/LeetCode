'''
Word Search
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

For example,
Given board =

[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
word = "ABCCED", -> returns true,
word = "SEE", -> returns true,
word = "ABCB", -> returns false.
'''

class Solution(object):
  def travel(self, board, word, i, j, visited):
    if len(word) == 0:
      return True

    nr, nc = len(board), len(board[0])
    for delta in [[0,1],[1,0],[0,-1],[-1,0]]:
      ii, jj = i-delta[0], j-delta[1]
      if 0<=ii<nr and 0<=jj<nc and not (ii,jj) in visited and board[ii][jj] == word[0]:
        copyV = visited.copy()
        copyV[(ii, jj)] = True
        if self.travel(board, word[1:], ii, jj, copyV):
          return True
    return False


  def exist(self, board, word):
    for i in xrange(len(board)):
      for j in xrange(len(board[0])):
        if board[i][j] == word[0]:
          if self.travel(board, word[1:], i, j, {(i,j):True}):
            return True
    return False

sol = Solution()
m = [['A','B','C','E'],['S','F','C','S'],['A','D','E','E']]
# m = [["C","A","A"], ["A","A","A"], ["B","C","D"]]
print sol.exist(m, "AAB")
print sol.exist(m,"SEE")
print sol.exist(m,"ABCB")