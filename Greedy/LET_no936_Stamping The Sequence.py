class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        stamp, target = list(stamp), list(target)
        m, n = len(stamp), len(target)
        res = []
        
        changed = True
        while changed:
            changed = False
            for i in range(n - m + 1):
                changed |= self.valid(target, i, stamp, res)
        
        return res[::-1] if target == ['?'] * n else []
    
    def valid(self, target, i, stamp, res):
        m = len(stamp)
        
        changed = False
        for j in range(m):
            if target[i+j] == '?':
                continue
            if target[i+j] != stamp[j]:
                return False
            changed = True
        
        if changed:
            target[i:i+m] = ['?'] * m
            res.append(i)
        return changed