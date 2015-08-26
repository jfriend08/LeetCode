'''
Remove all elements from a linked list of integers that have value val.

Example
Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
Return: 1 --> 2 --> 3 --> 4 --> 5

Credits:
Special thanks to @mithmatt for adding this problem and creating all test cases.
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
      if head == None:
        return head

      while (head) and (head.val == val):
        head = head.next

      runner = head

      while runner:
        if runner.next and runner.next.val == val:
          runner.next = runner.next.next
        else:
          runner = runner.next

      return head