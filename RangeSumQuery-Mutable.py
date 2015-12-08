'''
Given an integer array nums, find the sum of the elements between indices i and j (i <= j), inclusive.

The update(i, val) function modifies nums by updating the element at index i to val.
Example:
Given nums = [1, 3, 5]

sumRange(0, 2) -> 9
update(1, 2)
sumRange(0, 2) -> 8
Note:
The array is only modifiable by the update function.
You may assume the number of calls to update and sumRange function is distributed evenly.
'''

class NumArray(object):
  def __init__(self, nums):
    self.nums = nums

  def update(self, i, val):
    """
    :type i: int
    :type val: int
    :rtype: int
    """
    self.nums[i] = val

  def sumRange(self, i, j):
    """
    sum of elements nums[i..j], inclusive.
    :type i: int
    :type j: int
    :rtype: int
    """
    num = 0
    return sum(self.nums[i:j+1])



# Your NumArray object will be instantiated and called as such:
numArray = NumArray([1, 3, 5])
print numArray.sumRange(0, 2)
numArray.update(1, 2)
print numArray.sumRange(0, 2)