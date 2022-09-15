class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        memo = collections.defaultdict(int)
        res_left = res_right = 0
        left = 0
        for right in range(len(s)):
            memo[s[right]] += 1
            while len(memo) > 2 and left + 1 < right:
                memo[s[left]] -= 1
                if memo[s[left]] == 0:
                    del memo[s[left]]
                left += 1
            
            if right - left > res_right - res_left:
                res_left, res_right = left, right
        
        return res_right - res_left + 1