class Solution:
    def twoEggDrop(self, n: int) -> int:
        dp = [0] * (n + 1)
        return self.helper(dp, n)
    
    def helper(self, dp, n):
        if dp[n] != 0:
            return dp[n]
        
        dp[n] = n
        for i in range(1, n + 1):
            dp[n] = min(dp[n], 1 + max(i - 1, self.helper(dp, n - i)))
        
        """
        1. We lost an egg but we reduced the number of floors to i.
            Since we only have one egg left, we can just return i - 1 to check all floors.
        2. The egg did not break, and we reduced the number of floors to n - i.
            Solve this recursively to get the number of throws for n - i floors.
        """
        
        return dp[n]