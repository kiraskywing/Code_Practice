class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if k == 0:
            return 0
        
        memo = collections.defaultdict(int)
        left = res = 0
        for right, c in enumerate(s):
            memo[c] += 1
            while left < right and len(memo) > k:
                memo[s[left]] -= 1
                if memo[s[left]] == 0:
                    del memo[s[left]]
                left += 1
            res = max(res, right - left + 1)
        
        return res