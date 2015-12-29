'''
Given a linked list, swap every two adjacent nodes and return its head.

For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.

Your algorithm should use only constant space. You may not modify the values in the list,
only nodes itself can be changed.

Subscribe to see which companies asked this question
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
  def swapPairs(self, head):
    if not head:
      return
    elif head.next == None:
      return head
    """
    :type head: ListNode
    :rtype: ListNode
    """
    root = ListNode(None)
    prev = ListNode(None)
    root.next, prev.next = head.next, head
    late, fast = head, head.next

    while fast:
      # print prev.val, late.val, fast.val
      late.next = fast.next
      fast.next = late
      prev.next = fast

      if late.next == None:
        break
      prev = late
      fast = late.next.next
      late = late.next

    return root.next


n1, n2, n3, n4, n5 = ListNode(1), ListNode(2), ListNode(3), ListNode(4), ListNode(5)
#n1.next, n2.next, n3.next, n4.next = n2, n3, n4, n5
n1.next, n2.next = n2, n3
res = n1
sol = Solution()
res = sol.swapPairs(n1)

while not res == None:
  print res.val
  res = res.next
