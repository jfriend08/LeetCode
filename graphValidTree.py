'''
Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a
  pair of nodes), write a function to check whether these edges make up a valid tree.

For example:

Given n = 5 and edges = [[0, 1], [0, 2], [0, 3], [1, 4]], return true.

Given n = 5 and edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]], return false.

Hint:

Given n = 5 and edges = [[0, 1], [1, 2], [3, 4]], what should your return? Is this case a valid tree?
According to the definition of tree on Wikipedia: "a tree is an undirected graph in which any two
vertices are connected by exactly one path. In other words, any connected graph without simple cycles
is a tree."
Note: you can assume that no duplicate edges will appear in edges. Since all edges are undirected,
[0, 1] is the same as [1, 0] and thus will not appear together in edges.
'''

class Solution(object):
  def makeMap(self, n, edges, linkMap):
    for i in xrange(n):
      linkMap[i] = []
    for n1, n2 in edges:
      linkMap[n1] += [n2]
      linkMap[n2] += [n1]

  def isValidTravel(self, parent, node, linkMap, visited):
    visited[node] = True
    for nei in linkMap[node]:
      if nei == parent:
        continue
      elif not nei in visited:
        res = self.isValidTravel(node, nei, linkMap, visited)
        if not res:
          return res
      else:
        return False
    return True

  def validTree(self, n, edges):
    linkMap, visited = {}, {}
    self.makeMap(n, edges, linkMap)

    res = self.isValidTravel(None, 0, linkMap, visited)
    return len(visited.keys()) == n and res
    # for node in xrange(n):
    #   if not node in visited:
    #     res = self.isValidTravel(None, node, linkMap, visited)
    #     if res == False:
    #       return res
    # return True

sol = Solution()
n, edges = 5, [[0, 1], [0, 2], [0, 3], [1, 4]]
print sol.validTree(n, edges)

n, edges = 5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
print sol.validTree(n, edges)

n, edges = 5, [[0, 1], [1, 2], [3, 4]]
print sol.validTree(n, edges)