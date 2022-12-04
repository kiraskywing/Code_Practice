class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(1, n):
            nums[i] += nums[i - 1]
        
        diff = float('inf')
        res = 0
        for i in range(n):
            a = nums[i] // (i + 1)
            b = (nums[-1] - nums[i]) // (n - (i + 1)) if i != n - 1 else 0
            if abs(a - b) < diff:
                diff = abs(a - b)
                res = i
        
        return res