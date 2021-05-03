# https://leetcode.com/problems/merge-k-sorted-lists/
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import List
import heapq

# Runtime: 88 ms, faster than 97.46% of Python3 online submissions for Merge k Sorted Lists.
# Memory Usage: 18.1 MB, less than 48.53% of Python3 online submissions for Merge k Sorted Lists.
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        q = list((node.val, i, node) for i, node in enumerate(lists) if node)
        heapq.heapify(q)
        ans = curr = ListNode(0)
        while q:
            m, i, n = heapq.heappop(q)
            curr.next = n
            curr = curr.next
            if curr.next:
                heapq.heappush(q, (curr.next.val, i, curr.next))
        curr.next = None
        return ans.next
