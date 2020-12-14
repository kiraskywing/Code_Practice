# The same as Leetcode no.409 Longest Palindrome

class Solution:
    def longestPalindrome(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        
        odd = []
        res = 0
        
        for key, value in collections.Counter(s).items():
            if value % 2 == 0:
                res += value
            else:
                odd.append(value)
        
        if len(odd) > 0:
            res += sum(odd) - (len(odd) - 1)
        
        return res