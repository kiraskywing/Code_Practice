class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack = []
        for c in ops:
            if c == 'C':
                stack.pop()
            elif c == 'D':
                stack.append(stack[-1] * 2)
            elif c == '+':
                stack.append(stack[-1] + stack[-2])
            else:
                stack.append(int(c))
        return sum(stack)