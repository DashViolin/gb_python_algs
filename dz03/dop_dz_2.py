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

        tmp_nodes = [head]
        node = head
        while node.next:
            node = node.next
            tmp_nodes.append(node)
        middle = len(tmp_nodes) // 2
        return tmp_nodes[middle]
