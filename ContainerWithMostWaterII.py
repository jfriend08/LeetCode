'''
Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai).
n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).
Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container.
'''

class Solution(object):
    def maxArea(self, height):
      final_maxArea = 0
      for idx1 in range(len(height)):
        leftHeight = height[idx1]
        biggestSize = 0
        for idx2 in range(idx1+1, len(height)):
          rightHeight = height[idx2]
          if rightHeight >= leftHeight:
            area = leftHeight * (idx2-idx1)
          else:
            area = rightHeight * (idx2-idx1)
          if area > biggestSize:
            biggestSize = area
        if biggestSize > final_maxArea:
          final_maxArea = biggestSize
      return final_maxArea
