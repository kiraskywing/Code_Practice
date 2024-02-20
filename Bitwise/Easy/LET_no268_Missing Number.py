class Solution1:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)
        i = 0
        for num in nums:
            res ^= num
            res ^= i
            i += 1
        return res

class Solution2:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        total = (1 + n) * n // 2
        return total - sum(nums)
