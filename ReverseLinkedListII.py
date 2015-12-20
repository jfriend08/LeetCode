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
  def reverseBetween(self, head, m, n):
    if m == n:
      return head

    march = head
    prev = None
    i = 1

    set1 = []
    set2 = []

    while i <= n :
      if i == m:
        # print prev.val, march.val, '------1'
        set1 = [prev, march]
      elif i == n:
        # print prev.val, march.val, '------2'
        set2 = [prev, march]
      prev = march
      march = march.next
      i += 1


    set1[0].next = set2[1]
    set1[1].next = set2[1].next
    set2[0].next = set1[1]
    set2[1].next = set1[1].next

    return head


n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

sol = Solution()
result = sol.reverseBetween(n1, 2, 4)

while result.next != None:
  print result.val
  result = result.next



