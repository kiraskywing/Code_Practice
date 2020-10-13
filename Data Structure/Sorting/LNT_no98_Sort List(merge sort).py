"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
from random import randint
class Solution:
    """
    @param head: The head of linked list.
    @return: You should return the head of the sorted linked list, using constant space complexity.
    """
    def sortList(self, head):

        if not head or not head.next:
            return head

        fast, slow = head, head

        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        mid = slow.next
        slow.next = None

        list_1 = self.sortList(head)
        list_2 = self.sortList(mid)
        list_merged = self.merge(list_1, list_2)

        return list_merged

    def merge(self, list_1, list_2):

        dummy = ListNode(0)
        temp = dummy

        while list_1 and list_2:
            if list_1.val < list_2.val:
                temp.next = list_1
                temp = temp.next
                list_1 = list_1.next
            else:
                temp.next = list_2
                temp = temp.next
                list_2 = list_2.next

        if not list_1:
            temp.next = list_2
        if not list_2:
            temp.next = list_1

        return dummy.next