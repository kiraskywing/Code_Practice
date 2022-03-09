# The same as LeetCode no1597. Build Binary Expression Tree From Infix Expression

# Definition for a binary tree node.
# class Node(object):
#     def __init__(self, val=" ", left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def expTree(self, s: str) -> 'Node':
        nums, ops = [], []
        for c in s:
            if c.isdigit():
                nums.append(Node(val=c))
            elif c in "+-":
                while ops and ops[-1] in "+-*/":
                    self.mergeNums(nums, ops)
                ops.append(c)
            elif c in "*/":
                while ops and ops[-1] in "*/":
                    self.mergeNums(nums, ops)
                ops.append(c)
            elif c == '(':
                ops.append(c)
            elif c == ')':
                while ops[-1] != '(':
                    self.mergeNums(nums, ops)
                ops.pop()
        
        while ops:
            self.mergeNums(nums, ops)
        return nums[0]
    
    def mergeNums(self, nums, ops):
        op = ops.pop()
        r_node = nums.pop()
        l_node = nums.pop()
        nums.append(Node(val=op, left=l_node, right=r_node))