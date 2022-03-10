class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        cur, res = 0, float('-inf')
        for i in range(k - 1):
            cur += nums[i]
        for i in range(k - 1, len(nums)):
            cur += nums[i]
            res = max(res, cur)
            cur -= nums[i - k + 1]
        return res / k