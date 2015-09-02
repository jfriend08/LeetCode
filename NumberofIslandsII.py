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
  def numIslands(self, grid):
    if not grid:
      return 0
    m = len(grid)
    n = len(grid[0])
    self.visited = [[False for j in xrange(n)] for i in xrange(m)]
    islandCount = 0

    for i in range(m):
      for j in range(n):
        if grid[i][j] == '0' or self.visited[i][j]:
          continue
        else:
          self.visited[i][j] = True
          islandCount += 1
          self.travel(i,j,grid,m,n)
    return islandCount

  def travel(self,i,j,grid,m,n):
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    for idx in range(4):
      newX = i + dx[idx]
      newY = j + dy[idx]
      if newX < 0 or newX >= m or newY < 0 or newY >= n or grid[newX][newY] == '0' or self.visited[newX][newY]:
        continue
      else:
        self.visited[newX][newY] = True
        self.travel(newX,newY,grid,m,n)

if __name__ == "__main__":
    test = Solution()
    print test.numIslands(["11"])
