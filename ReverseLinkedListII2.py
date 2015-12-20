'''
Reverse a linked list from position m to n. Do it in-place and in one-pass.

For example:
Given 1->2->3->4->5->NULL, m = 2 and n = 4,

return 1->4->3->2->5->NULL.

Note:
Given m, n satisfy the following condition:
1 <= m <= n <= length of list.
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
  def reverseList(self, head):
    pre, cur, tail = None, head, head
    while cur != None:
      cur.next, pre, cur = pre, cur, cur.next
    return pre, tail

  def reverseBetween(self, head, m, n):
    if m > n:
      return head

    ohead = dummy = ListNode(0)
    whead = wtail = head
    dummy.next = head

    for i in xrange(n-m):
      wtail = wtail.next
    for i in xrange(m-1):
      ohead, whead, wtail = whead, whead.next, wtail.next

    otail, wtail.next = wtail.next, None
    rev_head, rev_tail = self.reverseList(whead)
    ohead.next, rev_tail.next = rev_head, otail
    return dummy.next

