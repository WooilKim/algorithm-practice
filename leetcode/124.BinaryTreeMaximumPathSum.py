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
        queue = deque()
        ans = root.val
        while queue:
            nodes = queue.popleft()
            left = nodes[0]
            if left.left:
                pass
            if left.right:
                pass
            if len(nodes) == 1:
                if left.left and left.right:
                    [left.left] + nodes + [left.right]
                right = nodes[1]


        pass


"""
Maxpath sum
start from every node
queue에 모든 노드를 넣고
부모로 갈 수가 없음
하나의 노드에서 두 자식이 다 0보다 크면 세개
queue에 
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

