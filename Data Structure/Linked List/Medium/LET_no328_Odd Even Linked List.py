"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    """
    @param head: a singly linked list
    @return: Modified linked list
    """

    def oddEvenList(self, head):

        if not head:
            return head

        odd, even = head, head.next
        evenhead = even

        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next

        odd.next = evenhead

        return head

class Solution2:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        dummy1, dummy2 = ListNode(-1), ListNode(-1)
        even_head, odd_head = dummy1, dummy2
        odd_turn = True
        
        while head:
            if odd_turn:
                odd_head.next = head
                odd_head = odd_head.next
            else:
                even_head.next = head
                even_head = even_head.next
            head = head.next
            odd_turn = not odd_turn
            
        odd_head.next = dummy1.next
        even_head.next = None
        
        return dummy2.next