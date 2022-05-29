class Solution:
    def maxProduct(self, words: List[str]) -> int:
        d = collections.defaultdict(int)
        for w in words:
            mask = 0
            for c in set(w):
                mask |= (1 << (ord(c) - ord('a')))
            d[mask] = max(d[mask], len(w))
        
        return max([d[x] * d[y] for x in d for y in d if not x & y] or [0])

class Solution2:
    def maxProduct(self, words: List[str]) -> int:
        memo = [set(w) for w in words]
        n = len(words)
        res = 0
        
        for i in range(n - 1):
            for j in range(i + 1, n):
                if not (memo[i] & memo[j]):
                    res = max(res, len(words[i]) * len(words[j]))
        
        return res