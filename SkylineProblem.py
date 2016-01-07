'''
A city's skyline is the outer contour of the silhouette formed by all the buildings in that city when viewed from a distance.
Now suppose you are given the locations and height of all the buildings as shown on a cityscape photo (Figure A), write a program
to output the skyline formed by these buildings collectively (Figure B).

The geometric information of each building is represented by a triplet of integers [Li, Ri, Hi], where Li and Ri are the x
coordinates of the left and right edge of the ith building, respectively, and Hi is its height. It is guaranteed that 0 <= Li,
Ri <= INT_MAX, 0 < Hi <= INT_MAX, and Ri - Li > 0. You may assume all buildings are perfect rectangles grounded on an absolutely flat surface at height 0.

For instance, the dimensions of all buildings in Figure A are recorded as: [ [2 9 10], [3 7 15], [5 12 12], [15 20 10], [19 24 8] ] .

The output is a list of "key points" (red dots in Figure B) in the format of [ [x1,y1], [x2, y2], [x3, y3], ... ] that uniquely
defines a skyline. A key point is the left endpoint of a horizontal line segment. Note that the last key point, where the rightmost
building ends, is merely used to mark the termination of the skyline, and always has zero height. Also, the ground in between any two
adjacent buildings should be considered part of the skyline contour.

For instance, the skyline in Figure B should be represented as:[ [2 10], [3 15], [7 12], [12 0], [15 10], [20 8], [24, 0] ].

Notes:

The number of buildings in any input list is guaranteed to be in the range [0, 10000].
The input list is already sorted in ascending order by the left x position Li.
The output list must be sorted by the x position.
There must be no consecutive horizontal lines of equal height in the output skyline. For instance, [...[2 3], [4 5], [7 5], [11 5], [12 7]...]
is not acceptable; the three lines of height 5 should be merged into one in the final output as such: [...[2 3], [4 5], [12 7], ...]
'''
import sys
class Solution(object):
  def findFirstHighIdx(self, hList):
    maxh, idx = -sys.maxint-1, -1
    for i in xrange(len(hList)):
      thish = hList[i]
      if thish > maxh:
        maxh, idx = thish, i
    return idx

  def getSkyline(self, buildings):
    """
    :type buildings: List[List[int]]
    :rtype: List[List[int]]
    """
    starts = [[elm[0], elm[2]] for elm in buildings]
    ends = [[elm[1], elm[2]] for elm in buildings]
    pos, curh = starts.pop(0)
    result, hList = [[pos, curh]], []

    while (len(ends)!=0 or len(starts)!=0) or pos != ends[-1][0]:
      print starts, ends, hList, result
      if len(starts) == 0:
        pos, nexth = ends.pop(0)
      elif starts[0][0] < ends[0][0]:
        pos, nexth = starts.pop(0)
        if nexth > curh: #next start building is higher
          curh = nexth
          result += [[pos,curh]]
        elif nexth <= curh: #next start building is equal or lower
          hList += [nexth]
      elif starts[0][0] > ends[0][0]: #next is end building
        pos, nexth = ends.pop(0)
        idx = self.findFirstHighIdx(hList)
        if idx != -1:
          nexth = hList[idx]
          hList.pop(idx)
          if nexth < curh:
            result += [[pos,nexth]]
          curh = nexth
        else:
          curh = 0
          result += [[pos,nexth]]

      elif starts[0][0] == ends[0][0]:
        pos, sh = starts.pop(0)
        pos, eh = ends.pop(0)
        idx = self.findFirstHighIdx(hList)
        nexth = (hList[idx] if idx != -1 else 0)
        if nexth > sh:
          hList.pop(0)
          hList += [sh]
          if nexth > curh:
            result += [[pos, nexth]]
          curh = nexth
        elif nexth <= sh:
          curh = sh
          result += [[pos, curh]]
    result += [[pos, 0]]
    return result

sol = Solution()
print sol.getSkyline([ [2,9,10], [3,7,15], [5,12,12], [15,20,10], [19,24,8] ])





