class Solution:
    """
    @param s: input string
    @return: the longest palindromic substring
    """

    def longestPalindrome(self, s):

        if not s:
            return ""

        longest = ""

        for middle in range(len(s)):

            sub = self.is_longestPalindrome(s, middle, middle)
            if len(sub) > len(longest):
                longest = sub

            sub = self.is_longestPalindrome(s, middle, middle + 1)
            if len(sub) > len(longest):
                longest = sub

        return longest

    def is_longestPalindrome(self, string, left, right):

        while left >= 0 and right < len(string) and string[left] == string[right]:
            left -= 1;
            right += 1

        return string[left + 1: right]