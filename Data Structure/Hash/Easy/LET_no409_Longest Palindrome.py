class Solution:
    def longestPalindrome(self, s: str) -> int:
        if not s:
            return 0

        res, odds = 0, 0
        for num in collections.Counter(s).values():
            res += num
            if num % 2:
                odds += 1
        if odds:
            res -= odds - 1
        
        return res