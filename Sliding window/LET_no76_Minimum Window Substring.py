class Solution:
    def minWindow(self, s: str, t: str) -> str:
        memo = collections.Counter(t)
        t_size = len(t)
        left, right, size = 0, 0, float('inf')
        res = ""
        
        while right < len(s):
            if memo[s[right]] > 0:
                t_size -= 1
            memo[s[right]] -= 1
            
            if t_size == 0:
                while left < right and memo[s[left]] < 0:
                    memo[s[left]] += 1
                    left += 1
                
                memo[s[left]] += 1
                t_size += 1
                if right - left + 1 < size:
                    res = s[left:right+1]
                    size = len(res)
                left += 1
            
            right += 1
            
        return res