'''
Given a binary tree, return the preorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
return [1,2,3].

Note: Recursive solution is trivial, could you do it iteratively?
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def travel(self, root):
        result = []
        if not root:
          return result
        result.append(root.val)
        result.extend(self.travel(root.left))
        result.extend(self.travel(root.right))
        return result

    def preorderTraversal(self, root):
        if not root:
          return []
        return self.travel(root)