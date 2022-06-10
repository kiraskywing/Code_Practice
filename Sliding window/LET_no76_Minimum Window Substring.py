class Solution:
    def minWindow(self, s: str, t: str) -> str:
        memo = collections.Counter(t)
        m, n = len(s), len(t)
        left = 0
        res_left, res_right = 0, m
        
        for right in range(m):
            if memo[s[right]] > 0:
                n -= 1
            memo[s[right]] -= 1
            
            if n == 0:
                while left < right and memo[s[left]] < 0:
                    memo[s[left]] += 1
                    left += 1
                
                if right - left < res_right - res_left:
                    res_left, res_right = left, right
                    
                memo[s[left]] += 1
                n += 1
                left += 1
        
        return s[res_left:res_right+1] if res_right - res_left < m else ""