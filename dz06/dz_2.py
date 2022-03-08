# https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: Node) -> Node:
        def get_next_layer(*nodes):
            next_nodes = []
            count = len(nodes)
            for i, node in enumerate(nodes):
                if node:
                    if i < count - 1:
                        node.next = nodes[i + 1]
                    if node.left:
                        next_nodes.append(node.left)
                    if node.right:
                        next_nodes.append(node.right)
            if next_nodes:
                return get_next_layer(*next_nodes)

        get_next_layer(root)
        return root
