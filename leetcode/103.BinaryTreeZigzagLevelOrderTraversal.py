# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

from typing import List
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Runtime: 28 ms, faster than 87.39% of Python3 online submissions for Binary Tree Zigzag Level Order Traversal.
# Memory Usage: 14.5 MB, less than 44.51% of Python3 online submissions for Binary Tree Zigzag Level Order Traversal.
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        ans, temp, stack, flag = list(), list(), deque(), 1
        if not root:
            return ans
        stack.append(root)
        while stack:
            for i in range(len(stack)):
                node = stack.popleft()
                temp.append(node.val)
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
            ans.append(temp[::flag])
            temp = list()
            flag *= -1
        return ans
