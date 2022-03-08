from typing import Optional


# https://leetcode.com/problems/middle-of-the-linked-list/
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # length = 0
        # node = head
        # while node.next:
        #     length += 1
        #     node = node.next
        # node = head
        # middle = round(length / 2 + 0.1)
        # for _ in range(middle):
        #     node = node.next
        # return node

        length = 0
        tmp_nodes = []
        node = head
        while node.next:
            length += 1
            tmp_nodes.append(node)
            node = node.next
        middle = round(length / 2 + 0.1)
        return tmp_nodes[middle]
