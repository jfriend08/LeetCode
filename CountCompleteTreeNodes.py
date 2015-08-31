'''
Given a complete binary tree, count the number of nodes.

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getLeftDepth (self, root):
      depth = 0
      while(root):
        depth += 1
        root = root.left
      return depth

    def getRightDepth (self, root):
      depth = 0
      while(root):
        depth += 1
        root = root.right
      return depth

    def countNodes(self, root):
      if not root:
        return 0

      left_d = self.getLeftDepth(root.left)
      right_d = self.getRightDepth(root.right)

      if left_d == right_d:
        return 2**(left_d+1) - 1
      else:
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)







