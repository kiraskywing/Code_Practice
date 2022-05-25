# The same as LeetCode no680. Valid Palindrome II

class Solution:
    """
    @param s: a string
    @return bool: whether you can make s a palindrome by deleting at most one character
    """

    def validPalindrome(self, s):
        return self.helper(s, 0, len(s) - 1, 1)
    
    def helper(self, s, left, right, times):
        if times < 0:
            return False
        
        while left <= right and s[left] == s[right]:
            left += 1
            right -= 1
        
        if left > right:
            return True
        return self.helper(s, left + 1, right, times - 1) or self.helper(s, left, right - 1, times - 1)