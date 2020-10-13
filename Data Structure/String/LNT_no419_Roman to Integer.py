class Solution:
    """
    @param s: Roman representation
    @return: an integer
    """

    def romanToInt(self, s):

        roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        res = roman[s[-1]]

        index = len(s) - 2

        while index >= 0:
            if roman[s[index]] < roman[s[index + 1]]:
                res -= roman[s[index]]
            else:
                res += roman[s[index]]
            index -= 1

        return res