'''
Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai).
n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).
Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container.
'''

class Solution(object):
    def maxArea(self, height):
      myMap = {}
      firstH = sys.minint
      secondH = sys.minint
      for idx in range(len(height)):
        eachH = height[idx]
        if eachH >= firstH:
          firstH = eachH
          myMap[firstH] = idx
        elif:
          eachH > firstH:


