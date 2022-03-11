from typing import Optional


# https://leetcode.com/problems/symmetric-tree/
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        left = []
        right = []

        def walk_left(node: Optional[TreeNode]):
            if node:
                left.append(node.val)
                walk_left(node.left)
                walk_left(node.right)
            else:
                left.append(None)

        def walk_right(node: Optional[TreeNode]):
            if node:
                right.append(node.val)
                walk_right(node.right)
                walk_right(node.left)
            else:
                right.append(None)

        walk_left(root.left)
        walk_right(root.right)
        return left == right
