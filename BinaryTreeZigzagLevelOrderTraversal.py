'''
Given a binary tree, return the zigzag level order traversal of its nodes' values.
(ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree {3,9,20,#,#,15,7},
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
confused what "{1,#,2,3}" means? > read more on how binary tree is serialized on OJ.
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
  def __init__(self):
    self.res = []

  def zigzagLevelHelper(self, root, level):
    print "level", level
    if not root:
      return

    if level == 0:
      self.res += [[root.val]]

    l, r = root.left, root.right

    if not l == None and not r == None:
      mylist = ([r.val, l.val] if level % 2 == 0 else [l.val, r.val])
    elif not l == None:
      mylist = [l.val]
    elif not r == None:
      mylist = [r.val]
    else:
      return

    if level % 2 == 0:
      try:
        self.res[level + 1] = mylist + self.res[level + 1]
      except:
        self.res = self.res + [mylist]
    elif level % 2 == 1:
      try:
        self.res[level + 1] = self.res[level + 1] + mylist
      except:
        self.res = self.res + [mylist]

    self.zigzagLevelHelper(root.left, level + 1)
    self.zigzagLevelHelper(root.right, level + 1)


  def zigzagLevelOrder(self, root):
    self.zigzagLevelHelper(root, 0)
    return self.res

