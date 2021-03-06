'''
Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.

Examples:
[2,3,4] , the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:

void addNum(int num) - Add a integer number from the data stream to the data structure.
double findMedian() - Return the median of all elements so far.
For example:

add(1)
add(2)
findMedian() -> 1.5
add(3)
findMedian() -> 2
'''
import bisect
class MedianFinder:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.myList = []
        self.lenth = None


    def addNum(self, num):
        """
        Adds a num into the data structure.
        :type num: int
        :rtype: void
        """
        bisect.insort(self.myList, num)
        self.lenth = len(self.myList)

    def findMedian(self):
        """
        Returns the median of current data stream
        :rtype: float
        """
        if self.lenth%2 == 1:
            return float(self.myList[(self.lenth-1)/2])
        else:
            upper_dix = self.lenth/2
            # print self.myList[upper_dix]
            # print self.myList[upper_dix-1]
            # result = (self.myList[upper_dix] + self.myList[upper_dix-1])/2
            # resul2 = float((2 + 3)/2.0)
            # print "result", result, "resul2", resul2
            return float((self.myList[upper_dix] + self.myList[upper_dix-1])/2.0)

    def getList(self):
        return self.myList


# Your MedianFinder object will be instantiated and called as such:
mf = MedianFinder()
mf.addNum(6)
print mf.findMedian()
print mf.getList()
mf.addNum(10)
print mf.findMedian()
print mf.getList()
mf.addNum(2)
print mf.findMedian()
print mf.getList()
mf.addNum(6)
print mf.findMedian()
print mf.getList()
mf.addNum(5)
print mf.findMedian()
print mf.getList()