# https://leetcode.com/problems/binary-tree-level-order-traversal/

from typing import List
from collections import defaultdict


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        ans = defaultdict(list)
        q = list()
        q.append((0, root))
        ans[0].append(root.val)
        while q:
            h, node = q.pop(0)
            if node.left:
                q.append((h + 1, node.left))
                ans[h + 1].append(node.left.val)
            if node.right:
                q.append((h + 1, node.right))
                ans[h + 1].append(node.right.val)

        return ans.values()
