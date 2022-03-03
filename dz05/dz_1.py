from typing import Optional, List


# https://leetcode.com/problems/binary-tree-postorder-traversal/
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def next_node(root: Optional[TreeNode]):
            if root:
                next_node(root.left)
                next_node(root.right)
                result.append(root.val)

        next_node(root)
        return result
