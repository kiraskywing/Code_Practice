from typing import (
    List,
)

class Solution:
    """
    @param expression: a list of strings
    @return: an integer
    """
    def evaluate_expression(self, expression: List[str]) -> int:
        if not expression:
            return 0
        
        nums, ops = [], []
        for s in expression:
            if s[0].isdigit():
                nums.append(int(s))
            elif s in "+-":
                while ops and ops[-1] in "+-*/":
                    self.mergeNums(nums, ops)
                ops.append(s)
            elif s in "*/":
                while ops and ops[-1] in "*/":
                    self.mergeNums(nums, ops)
                ops.append(s)
            elif s == '(':
                ops.append(s)
            elif s == ')':
                while ops[-1] != '(':
                    self.mergeNums(nums, ops)
                ops.pop()
        
        while ops:
            self.mergeNums(nums, ops)
        return nums[0] if nums else 0
    
    def mergeNums(self, nums, ops):
        op = ops.pop()
        r_val = nums.pop()
        l_val = nums.pop()
        if op == '+':
            nums.append(l_val + r_val)
        elif op == '-':
            nums.append(l_val - r_val)
        elif op == '*':
            nums.append(l_val * r_val)
        elif op == '/':
            nums.append(l_val // r_val)
