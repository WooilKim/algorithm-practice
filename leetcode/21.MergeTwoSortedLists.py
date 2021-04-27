# https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Runtime: 32 ms, faster than 90.31% of Python3 online submissions for Merge Two Sorted Lists.
# Memory Usage: 14.2 MB, less than 62.56% of Python3 online submissions for Merge Two Sorted Lists.
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        cur = ans = ListNode()
        while l1 or l2:
            if l1 and l2:
                if l1.val < l2.val:
                    cur.next = l1
                    l1 = l1.next
                else:
                    cur.next = l2
                    l2 = l2.next
            elif l1:
                cur.next = l1
                l1 = l1.next
            elif l2:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        return ans.next
