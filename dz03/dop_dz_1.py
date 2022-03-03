# https://leetcode.com/problems/delete-node-in-a-linked-list/
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        current_node = node
        while True:
            next_node = current_node.next
            current_node.val = next_node.val
            if not next_node.next:
                current_node.next = None
                break
            current_node = next_node
