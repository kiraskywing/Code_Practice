# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(-1, head)
        prev, last = dummy, dummy.next
        
        while last:
            cur = prev.next
            for _ in range(k):
                if last: 
                    last = last.next
                else:
                    return dummy.next
            
            prev2, last2 = cur, last
            for _ in range(k):
                temp = cur.next
                cur.next = last
                last = cur
                cur = temp
            
            prev.next = last
            prev, last = prev2, last2
            
        return dummy.next