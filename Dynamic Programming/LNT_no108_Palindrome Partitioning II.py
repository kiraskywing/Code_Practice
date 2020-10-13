class Solution:
    """
    @param s: A string
    @return: An integer
    """

    def minCut(self, s):
        if not s:
            return 0

        isPalindrome = self.getPalindrome(s)
        f = [i - 1 for i in range(len(s) + 1)]

        for length in range(1, len(s) + 1):
            for index in range(length):
                if isPalindrome[index][length - 1]:
                    f[length] = min(f[length], f[index] + 1)

        return f[len(s)]

    def getPalindrome(self, string):
        n = len(string)
        result = [[False for _ in range(n)] for _ in range(n)]

        for i in range(n):
            result[i][i] = True
            if i < n - 1:
                result[i][i + 1] = string[i] == string[i + 1]

        for length in range(2, n):
            for i in range(0, n - length):
                result[i][i + length] = result[i + 1][i + length - 1] and string[i] == string[i + length]

        return result
