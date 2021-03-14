class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        dp = collections.defaultdict(int)
        arr.sort()
        res = 0
        mod = 10 ** 9 + 7
        for i in range(len(arr)):
            dp[arr[i]] = 1
            for j in range(i):
                if arr[i] % arr[j] == 0:
                    dp[arr[i]] = (dp[arr[i]] + dp[arr[j]] * dp[arr[i] // arr[j]]) % mod
            res = (res + dp[arr[i]]) % mod
        return res