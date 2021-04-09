# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        if root.left:
            print(root.left)
            print(root.left.val)
            if root.left.val >= root.val:
                return False
        if root.right and root.right.val <= root.val:
            return False
        if self.isValidBST(root.left) and self.isValidBST(root.right):
            return True
        return True


def buildTree(root=List):
    root[0] = TreeNode(val=root[0])
    for i in range(len(root) // 2):
        root[i].left = root[i * 2 + 1] = TreeNode(val=root[i * 2 + 1])
        root[i].right = root[i * 2 + 2] = TreeNode(val=root[i * 2 + 2])
    return root[0]


if __name__ == '__main__':
    print(Solution().isValidBST(buildTree(root=[2, 1, 3])))
    print(Solution().isValidBST(buildTree(root=[5, 1, 4, None, None, 3, 6])))
    print(Solution().isValidBST(buildTree(root=[0])))
    print(Solution().isValidBST(buildTree(root=[5, 4, 6, None, None, 3, 7])))
