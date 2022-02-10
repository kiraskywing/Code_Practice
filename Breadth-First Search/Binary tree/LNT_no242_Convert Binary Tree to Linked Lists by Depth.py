"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
"""
class Solution:
    # @param {TreeNode} root the root of binary tree
    # @return {ListNode[]} a lists of linked list
    def binaryTreeToLists(self, root):
        if not root:
            return []
        
        res = []
        queue = collections.deque([root])
        while queue:
            dummy = ListNode(-1)
            head = dummy
            for _ in range(len(queue)):
                cur = queue.popleft()
                head.next = ListNode(cur.val)
                head = head.next
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            res.append(dummy.next)
        
        return res