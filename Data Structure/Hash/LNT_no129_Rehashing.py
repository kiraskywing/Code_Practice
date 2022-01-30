"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    """
    @param hashTable: A list of The first node of linked list
    @return: A list of The first node of linked list which have twice size
    """

    def rehashing(self, hashTable):
        HASH_SIZE = len(hashTable) * 2
        re_Table = [None for _ in range(HASH_SIZE)]

        for item in hashTable:
            cur = item
            while cur:
                self.addNode(re_Table, cur.val)
                cur = cur.next
        return re_Table

    def addNode(self, re_Table, key):
        new_key = key % len(re_Table)
        if re_Table[new_key] is None:
            re_Table[new_key] = ListNode(key)
        else:
            self.addListNode(re_Table[new_key], key)

    def addListNode(self, node, val):
        while node.next:
            node = node.next
        node.next = ListNode(val)