class Solution:
    def longestPalindrome(self, s: str) -> str:
        left = right = 0
        for k in range(len(s)):
            i, j = self.helper(s, k, k)
            if j - i > right - left:
                left, right = i, j
            
            if k > 0:
                i, j = self.helper(s, k - 1, k)
                if j - i > right - left:
                    left, right = i, j
        
        return s[left:right+1]
    
    def helper(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1, right - 1