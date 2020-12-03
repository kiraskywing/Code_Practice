# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.head = head
        

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        result, node, index = self.head, self.head.next, 1
        while node:
            if random.randint(0, index) == 0:
                result = node
            node = node.next
            index += 1
        return result.val

# Brief explanation for Reservoir Sampling: 
# https://leetcode.com/problems/linked-list-random-node/discuss/85659/Brief-explanation-for-Reservoir-Sampling
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()