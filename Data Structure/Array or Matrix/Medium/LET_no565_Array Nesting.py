class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            cur = 0
            j = i
            while nums[j] >= 0:
                cur += 1
                temp = nums[j]
                nums[j] = -1
                j = temp
            res = max(res, cur)
        return res