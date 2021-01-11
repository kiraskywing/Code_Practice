class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        stack1, stack2 = [], []
        max_val, min_val = max(x, y), min(x, y)
        first = 'a' if x > y else 'b'
        second = 'b' if x > y else 'a'
        res = 0
        
        for c in s:
            if stack1 and stack1[-1] == first and c == second:
                stack1.pop()
                res += max_val
            else:
                stack1.append(c)
        
        while stack1:
            c = stack1.pop()
            if stack2 and stack2[-1] == first and c == second:
                stack2.pop()
                res += min_val
            else:
                stack2.append(c)
        
        return res