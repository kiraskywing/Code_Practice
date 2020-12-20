class Solution:
    def reformatNumber(self, number: str) -> str:
        temp = [c for c in number if c.isdigit()]
        n, i, res = len(temp), 0, []
        
        while i < n:
            if i + 4 == n:
                res.append(''.join(temp[i:i+2]))
                i += 2
            elif i + 3 <= n:
                res.append(''.join(temp[i:i+3]))
                i += 3
            else:
                res.append(''.join(temp[i:]))
                i += 2
                
        return '-'.join(res)