# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        pre1, post1 = None, list1
        for i in range(b):
            if i == a - 1:
                pre1 = post1
            post1 = post1.next
        pre1.next = list2
        while list2.next:
            list2 = list2.next
        list2.next = post1.next
        post1.next = None
        
        return list1