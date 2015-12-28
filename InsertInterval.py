'''
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:
Given intervals [1,3],[6,9], insert and merge [2,5] in as [1,5],[6,9].

Example 2:
Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] in as [1,2],[3,10],[12,16].

This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].
'''

#Definition for an interval.
class Interval(object):
  def __init__(self, s=0, e=0):
    self.start = s
    self.end = e

import sys
class Solution(object):
  def isOverlapped(self, thisI, newI):
    order = sorted([thisI, newI], key = lambda x: x.start)
    if (order[1].start <= order[0].end):
      return True
    return False

  def getOverlappedIdxes(self, intervals, newInterval):
    idxs = []
    for i in xrange(len(intervals)):
      It = intervals[i]
      try:
        if i == len(intervals)-1 and It.end < newInterval.start:
          return True, [i]
        elif i ==0 and It.start > newInterval.end:
          return True, [i]
        elif newInterval.start > It.end and newInterval.end < intervals[i+1].start:
          return True, [i]
      except:
        pass
      if self.isOverlapped(It, newInterval):
        idxs.append(i)
    return False, idxs

  def merge(self, intervals, newInterval, idxs):
    allI = sorted([intervals[i] for i in idxs] + [newInterval], key = lambda x: x.start)
    start, end = allI[0].start, -sys.maxint - 1
    for it in allI:
      end = max(end, it.end)
    interval = Interval(start, end)
    return [interval]

  def insert(self, intervals, newInterval):
    """
    :type intervals: List[Interval]
    :type newInterval: Interval
    :rtype: List[Interval]
    """
    if not intervals:
      return [newInterval]
    intervals = sorted(intervals, key = lambda x: x.start)
    shouldInsert, idxs = self.getOverlappedIdxes(intervals, newInterval)
    if shouldInsert:
      return sorted(intervals[:idxs[0]+1] + [newInterval] + intervals[idxs[0]+1:], key = lambda x: x.start)
    else:
      fi, li = idxs[0], idxs[-1]
      return intervals[:fi] + self.merge(intervals, newInterval, idxs) + intervals[li+1:]


i1 = Interval(1,5)
# i2 = Interval(6,9)
newI = Interval(0,0)
# i1 = Interval(1,2)
# i2 = Interval(3,5)
# i3 = Interval(6,7)
# i4 = Interval(8,10)
# i5 = Interval(12,16)
# newI = Interval(4,9)

sol = Solution()
res = sol.insert([i1], newI)

for r in res:
  print r.start, r.end

