class Solution:
    def numberOfSpecialSubstrings(self, s: str) -> int:
        memo = collections.defaultdict(int)
        left, n = 0, len(s)
        res = 0
        for right, c in enumerate(s):
            memo[c] += 1
            while memo[c] > 1:
                memo[s[left]] -= 1
                left += 1
            
            res += right - left + 1
        
        return res
