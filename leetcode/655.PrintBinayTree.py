# https://leetcode.com/problems/print-binary-tree/
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def printTree(self, root: TreeNode) -> List[List[str]]:
        def get_height(node):
            return 0 if not node else 1 + max(get_height(node.left), get_height(node.right))

        def update_output(node, row, left, right):
            if not node:
                return
            mid = (left + right) // 2
            self.output[row][mid] = str(node.val)
            update_output(node.left, row + 1, left, mid - 1)
            update_output(node.right, row + 1, mid + 1, right)

        height = get_height(root)
        width = 2 ** height - 1
        self.output = [[''] * width for i in range(height)]
        update_output(node=root, row=0, left=0, right=width - 1)
        return self.output


def buildTree(root=List):
    root[0] = TreeNode(val=root[0])
    for i in range(len(root) // 2):
        root[i].left = root[i * 2 + 1] = TreeNode(val=root[i * 2 + 1])
        root[i].right = root[i * 2 + 2] = TreeNode(val=root[i * 2 + 2])
    return root[0]


if __name__ == '__main__':
    print(Solution().printTree(
        buildTree([7,
                   34, 46,
                   5, None, 7, None,
                   None, None, 38, 34, None, None, 25, 29,
                   28, 24, None, None, 13, 17])))

[
    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '7', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', '34', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '46', '', '', '', '', '', '', ''],
    ['', '', '', '5', '', '', '', '', '', '', '', 'None', '', '', '', '', '', '', '', '7', '', '', '', '', '', '', '', 'None', '', '', ''],
    ['', 'None', '', '', '', 'None', '', '', '', '38', '', '', '', '34', '', '', '', 'None', '', '', '', 'None', '', '', '', '25', '', '', '', '29', ''],
    ['28', '', '24', '', 'None', '', 'None', '', '13', '', '17', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']]

