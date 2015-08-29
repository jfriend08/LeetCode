'''
Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai).
n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).
Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container.
'''

class Solution(object):
    def maxArea(self, height):
      left_idx = 0
      right_idx = len(height)-1
      biggestArea = 0
      while left_idx < right_idx:
        left_height = height[left_idx]
        right_height = height[right_idx]
        biggestArea = max(biggestArea, min(left_height, right_height) * (right_idx - left_idx))
        if left_height <= right_height:
          left_idx += 1
        else:
          right_idx -= 1

      return biggestArea