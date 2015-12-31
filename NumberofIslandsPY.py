'''
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

11110
11010
11000
00000
Answer: 1

Example 2:

11000
11000
00100
00011
Answer: 3
'''
class Solution(object):
  def __init__(self):
    self.visited = {}
    self.grid = None
    self.islandC = 0

  def transverse(self, rS, cS):
    nr, nc = len(self.grid), len(self.grid[0])
    if rS < 0 or rS >= nr or cS <0 or cS >= nc:
      return

    if self.grid[rS][cS] == "0":
      return

    self.visited[(rS,cS)] = True
    self.transverse(rS+1,cS)
    self.transverse(rS,cS+1)

  def numIslands(self, grid):
    if not grid:
      return 0
    nr, nc, self.grid = len(grid), len(grid[0]), grid
    for i in xrange(nr):
      for j in xrange(nc):
        if self.grid[i][j] == "1" and not (i,j) in self.visited:
          self.visited[(i,j)] = True
          self.islandC += 1
          self.transverse(i,j)
    return self.islandC


m = [[1,1,1,1,0],[1,1,0,1,0],[1,1,0,0,0],[0,0,0,0,0]]
m = [[1,1,0,0,0],[1,1,0,0,0],[0,0,1,0,0],[0,0,0,1,1]]
m = ["1"]

sol = Solution()
print sol.numIslands(m)
