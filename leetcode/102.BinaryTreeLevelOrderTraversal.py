# https://leetcode.com/problems/binary-tree-level-order-traversal/

from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        ans = list()
        ans.append([root.val])
        curr = [root]
        next = list()
        h = 0
        while next:
            curr = [n for n in next]
            while curr:

            node = curr.pop(0)
            ans[h].append(node.val)
            next.append(curr.left)
