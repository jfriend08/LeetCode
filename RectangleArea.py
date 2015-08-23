"""
Find the total area covered by two rectilinear rectangles in a 2D plane.

Each rectangle is defined by its bottom left corner and top right corner as shown in the figure.

Rectangle Area
Assume that the total area is never beyond the maximum possible value of int.

Credits:
Special thanks to @mithmatt for adding this problem, creating the above image and all test cases.
"""


class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
      area1 = abs(A-C)*abs(B-D)
      area2 = abs(E-G)*abs(F-H)

      overlapedHeight = min(D,H) - max(B,F)
      overlapedWeight = min(C,G) - max(A,E)
      if overlapedHeight>0 and overlapedWeight>0:
        return area1 + area2 - overlapedHeight*overlapedWeight
      else:
        return area1 + area2
