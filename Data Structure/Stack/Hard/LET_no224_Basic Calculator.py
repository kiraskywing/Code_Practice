class Solution:
    def calculate(self, s: str) -> int:
        res = 0
        sign = [1, 1]
        
        i = 0
        while i < len(s):
            if s[i].isdigit():
                j = i
                while i < len(s) and s[i].isdigit():
                    i += 1
                res += int(s[j:i]) * sign.pop()
                continue
            
            elif s[i] == ')':
                sign.pop()
            elif s[i] != ' ':
                sign.append(-sign[-1] if s[i] == '-' else sign[-1])
            i += 1    
                
        return res