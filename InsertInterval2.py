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

class Solution(object):
  def insert(self, intervals, newInterval):
    s, e = newInterval.start, newInterval.end
    parts = merge, left, right = [], [], []
    for i in intervals:
      parts[(i.end < s) - (i.start > e)].append(i)
    if merge:
      s = min(s, merge[0].start)
      e = max(e, merge[-1].end)
    return left + [Interval(s, e)] + right


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

