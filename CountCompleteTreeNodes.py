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
    def __init__(self):
      self.depth = 0
      self.numLastNodes = 0

    def travel(self, root):

    def countNodes(self, root):
      if root == None:
        return 0

      self.travel(root)
      totalNum = 2**self.depth + self.numLastNodes
