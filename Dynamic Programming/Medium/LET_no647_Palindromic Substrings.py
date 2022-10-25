class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        is_palindrome = [[False for _ in range(n)] for _ in range(n)]
        
        res = 0
        for d in range(n):
            for left in range(n - d):
                right = left + d
                is_palindrome[left][right] = s[left] == s[right] and (right - left < 3 or is_palindrome[left + 1][right - 1])
                res += is_palindrome[left][right]
        
        return res