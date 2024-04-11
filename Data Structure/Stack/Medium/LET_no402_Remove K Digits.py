class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if k >= len(num):
            return "0"
        
        stack = []
        for c in num:
            while k and stack and stack[-1] > c:
                stack.pop()
                k -= 1
            stack.append(c)
        while k:
            stack.pop()
            k -= 1
        
        i = 0
        while i < len(stack) and stack[i] == '0':
            i += 1
        
        return ''.join(stack[i:]) if i < len(stack) else "0"