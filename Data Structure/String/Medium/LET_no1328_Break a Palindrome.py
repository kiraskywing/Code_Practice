class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        n = len(palindrome)
        palindrome = list(palindrome)
        for i in range(n // 2):
            if palindrome[i] != 'a':
                palindrome[i] = 'a'
                return ''.join(palindrome)
        palindrome[n - 1] = 'b'
        return ''.join(palindrome) if n >= 2 else ""