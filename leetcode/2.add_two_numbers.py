# https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Runtime: 56 ms, faster than 98.92% of Python3 online submissions for Add Two Numbers.
# Memory Usage: 14.3 MB, less than 43.71% of Python3 online submissions for Add Two Numbers.
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        cur = l1
        while cur or l2 or carry:
            if not cur:
                cur = ListNode()
            if l2:
                cur.val += l2.val
                l2 = l2.next
            cur.val += carry
            carry, cur.val = divmod(cur.val, 10)
            if not cur.next and (l2 or carry > 0):
                cur.next = ListNode()
            cur = cur.next
        return l1
