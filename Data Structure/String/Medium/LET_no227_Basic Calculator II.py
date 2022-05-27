class Solution:
    def calculate(self, s: str) -> int:
        res, num, pre, sign = 0, 0, 0, '+'
        for i in range(len(s)):
            if s[i].isdigit():
                num = 10 * num + int(s[i])
            if not s[i].isdigit() and s[i] != ' ' or i == len(s) - 1:
                if sign == '+':
                    res += num
                    pre = num
                elif sign == '-':
                    res -= num
                    pre = -num
                elif sign == '*':
                    res = res - pre + pre * num
                    pre *= num
                elif sign == '/':
                    res = res - pre + int(pre / num)
                    pre = int(pre / num)
                num = 0
                sign = s[i]
        
        return res