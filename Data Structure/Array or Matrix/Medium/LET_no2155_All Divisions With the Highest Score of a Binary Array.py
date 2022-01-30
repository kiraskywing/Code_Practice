class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        n, ones, zeros, mx = len(nums), sum(nums), 0, 0
        res = []
        for i in range(n + 1):
            cur = ones + zeros
            if cur > mx:
                mx = cur
                res = [i]
            elif cur == mx:
                res.append(i)
            if i < n:
                ones -= nums[i] == 1
                zeros += nums[i] == 0
        return res
        