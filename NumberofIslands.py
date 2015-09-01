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

Credits:
Special thanks to @mithmatt for adding this problem and creating all test cases.
'''

class Solution(object):
    def __init__(self):
      self.islandCount = 0

    def travel(self,i,j,n,m,visited):
      if self.grid[i][j] == '1' and not visited[i][j]:
        visited[i][j] = True
        dx = [0,1,0,-1]
        dy = [1,0,-1,0]
        for i in range(4):
          newI = i + dx[i]
          newJ = j + dy[i]
          if newI < 0 or newJ < 0 or newI >= n or newJ >= m:
            continue
          else:
            self.travel(newI,newJ,n,m,visited)
      else:
        visited[i][j] = True
        return

    def numIslands(self, grid):
      if not grid:
        return 0
      n = len(grid)
      m = len(grid[0])

      visited = [[False for x in range(m)] for x in range(n)]
      self.grid = grid

      for i in xrange(n):
        for j in xrange(m):
          if visited[i][j]:
            continue
          if not visited[i][j] and self.grid[i][j] == '1':
            self.islandCount += 1
            self.travel(i,j,n,m,visited)

      return self.islandCount









