class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        
        left = res = 0
        n = len(s)
        table = collections.defaultdict(int)
        
        for right in range(n):
            table[s[right]] += 1
            while left < right and table[s[right]] > 1:
                table[s[left]] -= 1
                left += 1
            res = max(res, right - left + 1)
        
        return res