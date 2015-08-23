"""
Invert a binary tree.

     4
   /   \
  2     7
 / \   / \
1   3 6   9
to
     4
   /   \
  7     2
 / \   / \
9   6 3   1
Trivia:
This problem was inspired by this original tweet by Max Howell:
Google: 90% of our engineers use the software you wrote (Homebrew), but you can’t invert a binary tree on a whiteboard so fuck off.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        left = None
        right = None
        if root != None:
          # recurrsion
          if root.left == None:
            tmpL = None
          elif root.left.left == None and root.left.right == None:
            tmpL = root.left
          else:
            tmpL = self.invertTree(root.left)

          if root.right == None:
            tmpR = None
          elif root.right.left == None and root.right.right ==None:
            tmpR = root.right
          else:
            tmpR = self.invertTree(root.right)

          root.left = tmpR
          root.right = tmpL

        return root
