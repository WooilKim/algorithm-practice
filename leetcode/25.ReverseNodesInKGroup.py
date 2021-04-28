# https://leetcode.com/problems/reverse-nodes-in-k-group/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Runtime: 52 ms, faster than 45.82% of Python3 online submissions for Reverse Nodes in k-Group.
# Memory Usage: 15.1 MB, less than 76.62% of Python3 online submissions for Reverse Nodes in k-Group.
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        curr = head
        q = list()
        if k == 1:
            return head
        flag = True
        tmp = None
        while curr:
            q.append(curr)
            curr = curr.next
            if len(q) == k:
                q[0].next = q[k - 1].next
                for i in range(1, k):
                    q[i].next = q[i - 1]
                if tmp:
                    tmp.next = q[k - 1]
                tmp = q[0]
                if flag:
                    head = q[k - 1]
                    flag = False
                q = list()
        return head
