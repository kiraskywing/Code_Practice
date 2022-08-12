class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if len(s) % 2 != 0:
            return False
        
        memo = {'[':']', '{':'}', '(':')'}
        for c in s:
            if c in "[({":
                stack.append(c)
            else:
                if not stack:
                    return False
                if memo[stack[-1]] != c:
                    return False
                else:
                    stack.pop()
        
        return len(stack) == 0