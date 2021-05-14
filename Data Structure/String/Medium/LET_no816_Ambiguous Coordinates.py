class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        n = len(s)
        res = []
        for i in range(1, n - 1):
            for a in self.helper(s[1 : 1 + i]):
                for b in self.helper(s[1 + i : n - 1]):
                    res.append("(" + a + ", " + b + ")")
        return res
    
    def helper(self, s):
        n = len(s)
        if n == 0 or n > 1 and s[0] == '0' and s[-1] == '0': return []
        if n > 1 and s[0] == '0': return ["0." + s[1 : ]]
        if n == 1 or s[-1] == '0': return [s]
        temp = [s]
        for i in range(1, n):
            temp.append(''.join(s[: i] + '.' + s[i : ]))
        return temp