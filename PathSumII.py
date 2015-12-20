'''
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
return
[
   [5,4,11,2],
   [5,8,4,5]
]
Subscribe to see which companies asked this question
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
  def pathSum(self, root, sum):
    if not root:
      return []

    # leaf case
    if not root.left and not root.right:
      if root.val == sum:
        return [[root.val]]
      else:
        return []

    result = []
    if root.left != None:
      result = [ [root.val] + elm for elm in self.pathSum(root.left, sum - root.val)]
    if root.right != None:
      result.extend([ [root.val] + elm for elm in self.pathSum(root.right, sum - root.val)])

    return result


n1 = TreeNode(1)
n2 = TreeNode(2)
n1.left = n2

sol = Solution()
print sol.pathSum(n1, 3)
