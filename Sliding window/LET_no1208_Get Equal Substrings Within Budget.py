class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        left = right = 0
        n = len(s)
        
        while right < n:
            maxCost -= abs(ord(s[right]) - ord(t[right]))
            if maxCost < 0:
                maxCost += abs(ord(s[left]) - ord(t[left]))
                left += 1
            right += 1
        
        return right - left
