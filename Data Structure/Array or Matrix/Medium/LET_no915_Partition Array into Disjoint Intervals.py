class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        leftMax = totalMax = nums[0]
        res = 0
        for i in range(1, len(nums)):
            totalMax = max(totalMax, nums[i])
            if nums[i] < leftMax:
                leftMax = totalMax
                res = i
        return res + 1