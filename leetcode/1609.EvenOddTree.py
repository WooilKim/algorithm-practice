# https://leetcode.com/problems/even-odd-tree/
import math
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return f'{self.left} {self.val} {self.right}'


class Solution:
    def isEvenOddTree(self, root: TreeNode) -> bool:
        if root is None:
            return True
        q = list()
        q.append([0, [root]])
        eo = [1, 0]
        while q:
            h, lv = q.pop(0)
            q.append([h + 1, list()])
            if (h + 1 % 2) == 0:
                prev = math.inf
            else:
                prev = -math.inf
            while lv:
                # print(lv)
                node = lv.pop(0)
                if node.val:
                    # strictly increasing or decreasing
                    if prev == node.val:
                        return False
                    if ((h + 1) % 2) == node.val % 2:
                        if node.val % 2 == 1:
                            # increasing order in even level
                            prev = max(prev, node.val)
                        else:
                            # decreasing order in odd level
                            prev = min(prev, node.val)
                    else:
                        # even odd error
                        return False
                if node.left:
                    q[0][1].append(node.left)
                if node.right:
                    q[0][1].append(node.right)
            if not q[0][1]:
                break
        return True


def buildTree(root=List):
    root[0] = TreeNode(val=root[0])
    for i in range(len(root) // 2):
        root[i].left = root[i * 2 + 1] = TreeNode(val=root[i * 2 + 1])
        root[i].right = root[i * 2 + 2] = TreeNode(val=root[i * 2 + 2])
    return root[0]


if __name__ == '__main__':
    print(Solution().isEvenOddTree(
        buildTree([7,
                   34, 46,
                   5, None, 7, None,
                   None, None, 38, 34,
                   None, None, 25, 29,
                   28, 24, None, None,
                   13, 17])))

