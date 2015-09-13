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

    def preorderTraversal(self, root):
        myQ = []
        result = []
        if not root:
          return []

        myQ.append(root)

        while myQ:
          curNode = myQ.pop()
          if curNode:
            result.append(curNode.val)
            myQ.append(curNode.right)
            myQ.append(curNode.left)
        return result



