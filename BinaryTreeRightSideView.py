'''
Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

For example:
Given the following binary tree,
   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
You should return [1, 3, 4].

Credits:
Special thanks to @amrsaqr for adding this problem and creating all test cases.
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
      self.rightSideArray = []

    def travel(self, root, depth):
      if root == None:
        return
      try:
        self.rightSideArray[depth] = root.val
      except:
        self.rightSideArray.append(root.val)

      self.travel(root.left, depth+1)
      self.travel(root.right, depth+1)

    def rightSideView(self, root):
        self.travel(root, 0)
        return self.rightSideArray;



