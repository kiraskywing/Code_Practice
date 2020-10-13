class Solution:
    """
    @param s: a string which consists of lowercase or uppercase letters
    @return: the length of the longest palindromes that can be built
    """

    def longestPalindrome(self, s):

        if len(s) < 2:
            return len(s)

        odd = []
        res = 0

        for char in set(s):
            if s.count(char) % 2 == 0:
                res += s.count(char)
            else:
                odd.append(s.count(char))

        if len(odd) > 0:
            return res + sum(odd) - (len(odd) - 1)
        else:
            return res