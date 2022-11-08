class Solution:
    def makeGood(self, s: str) -> str:
        res = []
        i = 0
        while i < len(s):
            if res and res[-1] != s[i] and res[-1].lower() == s[i].lower():
                res.pop()
                i += 1
                continue
            
            res.append(s[i])
            i += 1
                
        return ''.join(res)