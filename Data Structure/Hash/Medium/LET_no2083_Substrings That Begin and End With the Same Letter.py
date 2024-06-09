class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        memo = collections.defaultdict(int)
        res = 0
        for c in s:
            memo[c] += 1
            res += memo[c]
        
        return res