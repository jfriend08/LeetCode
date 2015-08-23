# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
      slowP = head
      fastP = head
      revP = None

      if fastP == None:
        return True
      elif fastP.next == None:
        return True

      while fastP != None and fastP.next != None:
        fastP = fastP.next.next
        tmpP = slowP.next
        slowP.next = revP
        revP = slowP
        slowP = tmpP

      if fastP != None:
        slowP = slowP.next

      while slowP != None and revP != None:
        if slowP.val != revP.val:
          return False
        revP = revP.next
        slowP = slowP.next
      return True