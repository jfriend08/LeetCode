'''
My Submissions Question Solution
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes v and w as the lowest node in T that has both v and w as descendants (where we allow a node to be a descendant of itself).”

        _______3______
       /              \
    ___5__          ___1__
   /      \        /      \
   6      _2       0       8
         /  \
         7   4
For example, the lowest common ancestor (LCA) of nodes 5 and 1 is 3. Another example is LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.val1AncList = []
        self.val2AncList = []

    def travel(self, root, p, q, path):
        if not root:
          return
        path.append(root.val)
        if root.val == p.val:
          self.val1AncList = path[:]
        if root.val == q.val:
          self.val2AncList = path[:]

        self.travel(root.left,p,q,path)
        self.travel(root.right,p,q,path)
        path.pop(-1)

    def getLCA(self):
        print self.val1AncList
        print self.val2AncList
        if not self.val1AncList or not self.val2AncList:
          return

        sameVal = None
        for idx in range(min(len(self.val1AncList), len(self.val2AncList))):
          if self.val1AncList[idx] == self.val2AncList[idx]:
            sameVal = self.val1AncList[idx]
        return sameVal

    def lowestCommonAncestor(self, root, p, q):
        if p == root or q == root:
          return root
        self.travel(root,p,q,[])
        return self.getLCA()