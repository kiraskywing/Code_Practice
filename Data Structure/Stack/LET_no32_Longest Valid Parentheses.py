class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        res = 0
        stack = []
        for i, c in enumerate(s):
            if c == '(': 
                stack.append(i)
            else:
                if stack and s[stack[-1]] == '(': 
                    stack.pop()
                else: 
                    stack.append(i)
                    
        if not stack: 
            res = n
        else:
            a, b = n, 0
            while stack:
                b = stack.pop()
                res = max(res, a - b - 1)
                a = b
            res = max(res, a)
        
        return res