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
  def numIslands(self, grid):
    if not grid:
      return 0

    nr, nc, count = len(grid), len(grid[0]), 0
    for i in xrange(nr):
      for j in xrange(nc):
        if grid[i][j] == "0":
          continue
        else:
          count += 1
          stack = list()
          stack.append([i,j])

          while len(stack) != 0:
            i_tmp, j_tmp = stack.pop()
            if i_tmp > 0 and grid[i_tmp-1][j_tmp] == "1":
              stack.append([i_tmp-1, j_tmp])
            if i_tmp < nr-1 and grid[i_tmp+1][j_tmp] == "1":
              stack.append([i_tmp+1, j_tmp])
            if j_tmp > 0 and grid[i_tmp][j_tmp-1] == "1":
              stack.append([i_tmp, j_tmp-1])
            if j_tmp < nc-1 and grid[i_tmp][j_tmp+1] == "1":
              stack.append([i_tmp,j_tmp+1])
            grid[i_tmp][j_tmp] = "0"

    return count

m = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
m = [["1", "1", "1"],["1","0","1"],["1","1","1"]]
m = [["1", "1", "1"],["0","1","0"],["1","1","1"]]
sol = Solution()
print sol.numIslands(m)



