class Solution:
    def numberOfMatches(self, n: int) -> int:
        res = 0
        while n >= 2:
            res += n // 2
            n = n // 2 + n % 2
        return res

        # Solution 2:
        return n - 1
        # n teams, one match, one lose and eliminated.
        # The champion never lose, n - 1 other team lose.
        # So need n - 1 match.