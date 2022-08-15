class Solution:
    def validPalindrome(self, s: str) -> bool:
        return self.helper(s, 0, len(s) - 1, 1)
    
    def helper(self, s, left, right, times):
        while left < right and s[left] == s[right]:
            left += 1
            right -= 1
            
        if left >= right:
            return True
        
        if times != 0:
            return self.helper(s, left + 1, right, 0) or self.helper(s, left, right - 1, 0)
        return False