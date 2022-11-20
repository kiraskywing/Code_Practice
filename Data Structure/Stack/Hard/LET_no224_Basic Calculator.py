class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        res, sign, num = 0, 1, 0
        for c in s:
            if c.isdigit():
                num = 10 * num + int(c)
            elif c == '+':
                res += sign * num
                sign = 1
                num = 0
            elif c == '-':
                res += sign * num
                sign = -1
                num = 0
            elif c == '(':
                stack.append((res, sign))
                sign = 1
                res = 0
            elif c == ')':
                res += sign * num
                num = 0
                prev_res, prev_sign = stack.pop()
                res *= prev_sign
                res += prev_res
        
        if num > 0:
            res += sign * num
        
        return res