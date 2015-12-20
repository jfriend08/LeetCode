'''
Follow up for H-Index: What if the citations array is sorted in ascending order? Could you optimize your algorithm?

Hint:

Expected runtime complexity is in O(log n) and the input is sorted.
'''

class Solution(object):
  def hIndex(self, citations):
    if len(citations)==1:
      return min(citations[0], 1)
    if len(citations)==0:
      return 0

    n = len(citations)
    idxl = 0
    idxr = n-1

    while idxl <= idxr:
      idxm = (idxl+idxr)/2
      if citations[idxm] < n-idxm:
        idxl = idxm + 1
      else:
        idxr = idxm - 1
    return n-idxl


sol = Solution()
print sol.hIndex([1,1,2,3,4,5,7])
# print sol.hIndex([11,15])
# print sol.hIndex([0,1,3,5,6])
# print sol.hIndex([100])
# print sol.hIndex([0,0])
# print sol.hIndex([0,1])
# print sol.hIndex([1,2])
# print sol.hIndex([])
