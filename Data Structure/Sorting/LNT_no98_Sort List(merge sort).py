# The same problem as Leetcode 148. Sort List

"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param head: The head of linked list.
    @return: You should return the head of the sorted linked list, using constant space complexity.
    """
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        fast = slow = head
        
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            
        mid = slow.next
        slow.next = None
        
        lst_1 = self.sortList(head)
        lst_2 = self.sortList(mid)
        merged = self.merge(lst_1, lst_2)
        
        return merged
    
    def merge(self, lst_1, lst_2):
        dummy = ListNode(0)
        temp = dummy
        
        while lst_1 and lst_2:
            if lst_1.val < lst_2.val:
                temp.next = lst_1
                lst_1 = lst_1.next
            else:
                temp.next = lst_2
                lst_2 = lst_2.next
            temp = temp.next
        
        if lst_1:
            temp.next = lst_1
        if lst_2:
            temp.next = lst_2
        
        return dummy.next