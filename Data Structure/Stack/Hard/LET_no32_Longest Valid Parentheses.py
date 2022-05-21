class Solution:
    def longestValidParentheses(self, s: str) -> int:
        res = 0
        stack = []
        for i, c in enumerate(s):
            if c == ')':
                if stack and s[stack[-1]] == '(':
                    stack.pop()
                    res = max(res, i - stack[-1] if stack else i + 1)
                else:
                    stack.append(i)
            else:
                stack.append(i)
        
        return res