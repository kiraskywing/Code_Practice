class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        memo = collections.Counter(p)
        m, n = len(s), len(p)
        if n > m:
            return []
        
        for i in range(n - 1):
            if s[i] in memo:
                memo[s[i]] -= 1
        
        res = []
        for i in range(n - 1, m):
            if s[i] in memo:
                memo[s[i]] -= 1
            if i >= n and s[i - n] in memo:
                memo[s[i - n]] += 1
            if all(v == 0 for v in memo.values()):
                res.append(i - n + 1)
        return res