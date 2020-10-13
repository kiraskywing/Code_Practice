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
        for i in range(1, n):
            is_Palindrome[i][i - 1] = True

        longest, start, end = 1, 0, 0
        for diff in range(1, n):
            for left in range(n - diff):
                right = left + diff
                is_Palindrome[left][right] = s[left] == s[right] and is_Palindrome[left + 1][right - 1]
                if is_Palindrome[left][right] and diff + 1 > longest:
                    longest = diff + 1
                    start, end = left, right

        return s[start: end + 1]