'''
Minimum Height Trees
For a undirected graph with tree characteristics, we can choose any node as the root.
The result graph is then a rooted tree. Among all possible rooted trees, those with minimum
height are called minimum height trees (MHTs). Given such a graph, write a function to find
all the MHTs and return a list of their root labels.

Format
The graph contains n nodes which are labeled from 0 to n - 1. You will be given the number n
and a list of undirected edges (each edge is a pair of labels).

You can assume that no duplicate edges will appear in edges. Since all edges are undirected,
[0, 1] is the same as [1, 0] and thus will not appear together in edges.

Example 1:

Given n = 4, edges = [[1, 0], [1, 2], [1, 3]]

        0
        |
        1
       / \
      2   3
return [1]

Example 2:

Given n = 6, edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]

     0  1  2
      \ | /
        3
        |
        4
        |
        5
return [3, 4]

Hint:

How many MHTs can a graph have at most?
'''

class Solution(object):
  def getMap(self, n, edges, linkMap):
    for i in xrange(n):
      linkMap[i] = set()
    for n1, n2 in edges:
      linkMap[n1].add(n2)
      linkMap[n2].add(n1)

  def findMinHeightTrees(self, n, edges):
    linkMap = {}
    self.getMap(n, edges, linkMap)
    while len(linkMap) > 2:
      allLeaves = [ n1 for n1 in linkMap.keys() if len(linkMap[n1])==1 ]
      for n1 in allLeaves:
        n2 = list(linkMap[n1])[0]
        del linkMap[n1]
        linkMap[n2].discard(n1)
    return linkMap.keys()

sol = Solution()
n, edges = 4, [[1, 0], [1, 2], [1, 3]]
print sol.findMinHeightTrees(n, edges)

n, edges = 6, [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]
print sol.findMinHeightTrees(n, edges)













