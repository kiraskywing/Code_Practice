class Solution:
    def minDeletions(self, s: str) -> int:
        count = collections.Counter(s)
        rec = set()
        res = 0
        
        for c, i in count.items():
            while i in rec:
                i -= 1
                res += 1
            if i > 0:
                rec.add(i)
        
        return res