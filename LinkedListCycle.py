'''
Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?Linked List Cycle
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        if not head or not head.next:
          return False
        fastP = head.next.next
        slowP = head
        while fastP != slowP:
          if fastP == None or slowP == None or fastP.next == None:
            return False
          fastP = fastP.next.next
          slowP = slowP.next
        return True
