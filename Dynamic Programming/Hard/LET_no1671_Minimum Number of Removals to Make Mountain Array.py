class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        if len(nums) <= 3:
            return 0
        
        n = len(nums)
        increase, decrease = [0] * n, [0] * n
        
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    increase[i] = max(increase[i], increase[j] + 1)
                    
        for i in range(n - 2, -1, -1):
            for j in range(n - 1, i, -1):
                if nums[i] > nums[j]:
                    decrease[i] = max(decrease[i], decrease[j] + 1)
        
        res = 0
        for i in range(1, n - 1):
            if increase[i] and decrease[i]:
                res = max(res, increase[i] + decrease[i] + 1)
        
        return n - res