'''
Sort a linked list in O(n log n) time using constant space complexity.
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
  def sortList(self, head):
    print head.val
    """
    :type head: ListNode
    :rtype: ListNode
    """
    if not head or not head.next:
      return head

    fast, slow = head, head

    while fast.next and fast.next.next:
      fast = fast.next.next
      slow = slow.next

    l, r, slow.next = head, slow.next, None
    l = self.sortList(l)
    r = self.sortList(r)
    return self.merge(l, r)

  def merge(self, l, r):
    if not l or not r:
      return l or r

    if l.val > r.val:
      l, r = r, l

    root = prev = l
    l = l.next
    while l and r:
      if l.val < r.val:
        prev.next = l
        l = l.next
      else:
        prev.next = r
        r = r.next
      prev = prev.next

    prev.next = l or r
    return root


n1 = ListNode(2)
n2 = ListNode(1)
n1.next = n2

sol = Solution()
sol.sortList(n1)

