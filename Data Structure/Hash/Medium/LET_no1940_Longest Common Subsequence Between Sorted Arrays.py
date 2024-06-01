class Solution:
    def longestCommonSubsequence(self, arrays: List[List[int]]) -> List[int]:
        memo = dict()
        for num in arrays[0]:
            memo[num] = 1

        n = len(arrays)
        for i in range(1, n):
            for num in arrays[i]:
                if num in memo:
                    memo[num] += 1

        res = []
        for num, val in memo.items():
            if val == n:
                res.append(num)

        return res