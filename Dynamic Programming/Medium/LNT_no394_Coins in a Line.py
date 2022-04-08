class Solution:
    """
    @param n: An integer
    @return: A boolean which equals to true if the first player will win
    """
    def first_will_win(self, n: int) -> bool:
        dp = [False] * 3
        dp[2] = dp[1] = True
        for i in range(3, n + 1):
            dp[i % 3] = not dp[(i - 1) % 3] or not dp[(i - 2) % 3]
        return dp[n % 3]

        # O(1) solution:
        return n % 3 != 0
