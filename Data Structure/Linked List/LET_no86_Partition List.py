# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        temp1, temp2 = ListNode(-1), ListNode(-1)
        front, back = temp1, temp2
        while head:
            if head.val < x:
                front.next = head
                front = front.next
            else:
                back.next = head
                back = back.next
            head = head.next
        back.next = None
        front.next = temp2.next
        return temp1.next