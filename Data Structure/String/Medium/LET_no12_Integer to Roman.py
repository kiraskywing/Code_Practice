class Solution:
    """
    @param n: The integer
    @return: Roman representation
    """

    def intToRoman(self, n):
        i = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        j = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

        res = []

        for char, val in zip(i, j):
            res.append(char * (n // val))
            n %= val

        return "".join(res)
