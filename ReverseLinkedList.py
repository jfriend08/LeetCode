'''
Reverse a singly linked list.
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
      marchingP = head
      previousP = None
      returnP = None
      while marchingP:
        tmp = marchingP.next
        marchingP.next = previousP
        previousP = marchingP
        marchingP = tmp

      return previousP