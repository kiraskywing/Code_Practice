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

class Solution2:
    def minDeletions(self, s: str) -> int:
        memo = collections.Counter(s)
        freqs = sorted([f for f in memo.values()], reverse=True)
        
        max_freq = len(s)
        res = 0
        
        for freq in freqs:
            if freq > max_freq:
                res += freq - max_freq
                freq = max_freq
            
            max_freq = max(0, freq - 1)
            
        return res