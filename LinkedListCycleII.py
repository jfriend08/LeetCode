'''
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

Note: Do not modify the linked list.

Follow up:
Can you solve it without using extra space?
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
  def detectCycle(self, head):
    pf, ps, pl = head, head, head
    try:
      ps = ps.next
      pf = pf.next.next
    except:
      return None

    while pf != ps:
      try:
        ps = ps.next
        pf = pf.next.next
      except:
        return None

    count = 1
    cNodes = [ps]
    ps = ps.next
    while not ps in cNodes:
      cNodes.append(ps)
      ps = ps.next
      count += 1

    while not pl in cNodes:
      pl = pl.next

    return pl

