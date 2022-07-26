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


class Solution2:
    def expTree(self, s: str) -> 'Node':
        tokens = collections.deque(list(s))
        return self.parser(tokens)
    
    def parser(self, tokens):
        lhs = self.parseTerm(tokens)
        while tokens and tokens[0] in "+-":
            op = tokens.popleft()
            rhs = self.parseTerm(tokens)
            lhs = Node(val=op, left=lhs, right=rhs)
            
        return lhs
    
    def parseTerm(self, tokens):
        lhs = self.parseFactor(tokens)
        while tokens and tokens[0] in "*/":
            op = tokens.popleft()
            rhs = self.parseFactor(tokens)
            lhs = Node(val=op, left=lhs, right=rhs)
            
        return lhs
    
    def parseFactor(self, tokens):
        if tokens[0] == '(':
            tokens.popleft()    # consume '('
            node = self.parser(tokens)
            tokens.popleft()    # consume ')'
            return node
        
        cur = tokens.popleft()
        return Node(val=cur)