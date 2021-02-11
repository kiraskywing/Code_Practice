# The same as LeetCode no138. Copy List with Random Pointer

"""
Definition for singly-linked list with a random pointer.
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
"""


class Solution:
    # @param head: A RandomListNode
    # @return: A RandomListNode
    def copyRandomList(self, head):
        if not head:
            return None

        Map = {}
        clone_head = RandomListNode(head.label)
        Map[head] = clone_head

        p1, p2 = head, clone_head
        while p1:
            p2.random = p1.random
            if p1.next:
                p2.next = RandomListNode(p1.next.label)
                Map[p1.next] = p2.next
            else:
                p2.next = None
            p1 = p1.next
            p2 = p2.next

        p2 = clone_head
        while p2:
            if p2.random:
                p2.random = Map[p2.random]
            p2 = p2.next
        return clone_head
