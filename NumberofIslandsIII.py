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
    visited = [[False for j in range(n)] for i in range(m)]
    queue = []
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    islandCount = 0

    for i in range(m):
      for j in range(n):
        if grid[i][j] == '0' or visited[i][j]:
          continue
        islandCount += 1
        queue.append((i,j))
        while queue:
          (x,y) = queue.pop()
          visited[x][y] = True
          for idx in range(4):
            nx = x + dx[idx]
            ny = y + dy[idx]
            if nx < 0 or nx >= m or ny < 0 or ny >= n or grid[nx][ny] == '0' or visited[nx][ny]:
              continue
            else:
              queue.append((nx,ny))

    return islandCount

if __name__ == "__main__":
    test = Solution()
    print test.numIslands(["11111111"])
