# https://leetcode.com/problems/distribute-coins-in-binary-tree/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def distributeCoins(self, root: TreeNode) -> int:
        def dfs(node):
            if not node: return 0, 0
            (lbal, lcnt), (rbal, rcnt) = dfs(node.left), dfs(node.right)
            bal = node.val + lbal + rbal - 1
            return bal, lcnt + rcnt + abs(bal)
        return dfs(root)[1]
