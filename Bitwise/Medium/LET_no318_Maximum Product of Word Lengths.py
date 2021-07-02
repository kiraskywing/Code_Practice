class Solution:
    def maxProduct(self, words: List[str]) -> int:
        d = collections.defaultdict(int)
        for w in words:
            mask = 0
            for c in set(w):
                mask |= (1 << (ord(c) - ord('a')))
            d[mask] = max(d[mask], len(w))
        
        return max([d[x] * d[y] for x in d for y in d if not x & y] or [0])