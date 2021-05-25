# https://leetcode.com/problems/binary-tree-maximum-path-sum/

from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        max_path = float("-inf")  # placeholder to be updated

        def get_max_gain(node):
            nonlocal max_path  # This tells that max_path is not a local variable
            if node is None:
                return 0
            gain_on_left = max(get_max_gain(node.left), 0)  # Read the part important observations
            gain_on_right = max(get_max_gain(node.right), 0)  # Read the part important observations
            current_max_path = node.val + gain_on_left + gain_on_right  # Read first three images of going down the recursion stack
            max_path = max(max_path, current_max_path)  # Read first three images of going down the recursion stack

            return node.val + max(gain_on_left, gain_on_right)  # Read the last image of going down the recursion stack

        get_max_gain(root)  # Starts the recursion chain
        return max_path


# [-4,4-5,-2,-3,None,3,1,8,6,7,9,10]

"""
Maxpath sum
start from every node
queue에 모든 노드를 넣고
부모로 갈 수가 없음
하나의 노드에서 두 자식이 다 0보다 크면 세개
queue에 
dp[node] = node로 시작하는 제일 긴 path

 
[[root]]
[[root][left][right][left,root][left,root,right],[root,right]]
[[ll,left], [lr, left], [ll,l,r],[lr,l]

while queue:
    l = queue.popleft()
    mem + l[0].left 
    if l[0].left and [l[0].left]+l not in mem:
        queue.append([l[0]]+l)
    if l[0].right
    if l[-1].left
    if l[-1].right and l + [l[-1].right] not in mem:
        queue.append(l + [l[-1].right])
    if left + l + right not in mem:
        
dic
sum, root
"""
