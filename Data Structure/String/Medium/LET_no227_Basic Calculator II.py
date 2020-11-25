class Solution:
    def calculate(self, s: str) -> int:
        num, sign, stack = 0, '+', []
        
        for i in range(len(s)):
            if s[i].isdigit():
                num = num * 10 + int(s[i])
            if not s[i].isdigit() and s[i] != ' ' or i == len(s) - 1:
                if sign == '+':
                    stack.append(num)
                if sign == '-':
                    stack.append(-num)
                if sign == '*':
                    stack.append(stack.pop() * num)
                if sign == '/':
                    pre = stack.pop()
                    if pre < 0:
                        pre = -(-pre // num)    # -3 // 2 = -2
                    else:
                        pre //= num
                    stack.append(pre)
                
                sign = s[i]
                num = 0
        
        return sum(stack)