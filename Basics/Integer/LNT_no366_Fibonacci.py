class Solution:
    """
    @param n: an integer
    @return: an integer f(n)
    """

    def fibonacci(self, n):
        a, b, temp = 0, 1, 0
        if n == 1:
            return 0
        if n == 2:
            return 1

        for i in range(3, n + 1):
            temp = b
            b += a
            a = temp
        return b

        """
        return self.fibonacci(n-2) + self.fibonacci(n-1)
        """

if __name__ == '__main__':
    ans = Solution()
    print(ans.fibonacci(3))