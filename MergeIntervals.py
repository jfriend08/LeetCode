'''
Given a collection of intervals, merge all overlapping intervals.

For example,
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18].
'''

class Interval(object):
  def __init__(self, s=0, e=0):
    self.start = s
    self.end = e

class Solution(object):
  def merge(self, intervals):
    """
    :type intervals: List[Interval]
    :rtype: List[Interval]
    """
    if not intervals:
      return []
    sorted(intervals, key=lambda x: x.start)
    mRes = [intervals[0]]

    # print mRes[0].start, mRes[0].end

    for i in xrange(1, len(intervals)):
      testI = intervals[i]
      resI = mRes[-1]
      if testI.start <= resI.end:
        resI.end = max(resI.end, testI.end)
      else:
        mRes.append(testI)
      # if testI.start > resI.end:
      #   mRes.append(testI)
      # else:
      #   resI.start = min(resI.start, testI.start)
      #   resI.end = max(resI.end, testI.end)

    return mRes


sol = Solution()
# i1, i2, i3, i4 = Interval(1,3), Interval(2,6), Interval(8,10), Interval(15,18)
i1, i2 = Interval(0,0), Interval(1,4)

res = sol.merge([i1, i2])

print "lenght", len(res)
for elm in res:
  print elm.start, elm.end
