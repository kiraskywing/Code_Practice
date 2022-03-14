# The same as LeetCode no5. Longest Palindromic Substring

class Solution:
    """
    @param s: input string
    @return: the longest palindromic substring
    """

    def longestPalindrome(self, s):
        if not s:
            return ""

        n = len(s)
        is_Palindrome = [[False] * n for _ in range(n)]

        for i in range(n):
            is_Palindrome[i][i] = True
            if i > 0:
                is_Palindrome[i][i - 1] = True

        start, end = 0, 0
        for diff in range(1, n):
            for left in range(n - diff):
                right = left + diff
                if s[left] == s[right] and is_Palindrome[left + 1][right - 1]:
                    is_Palindrome[left][right] = True
                    if right - left > end - start:
                        start, end = left, right

        return s[start: end + 1]