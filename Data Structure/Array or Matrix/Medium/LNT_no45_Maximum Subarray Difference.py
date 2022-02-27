from typing import (
    List,
)

class Solution:
    """
    @param nums: A list of integers
    @return: An integer indicate the value of maximum difference between two substrings
    """
    def max_diff_sub_arrays(self, nums: List[int]) -> int:
        if not nums:
            return 0

        n = len(nums)
        left_min, left_max = [0] * n, [0] * n
        right_min, right_max = [0] * n, [0] * n
        self.getPreSum(left_min, left_max, nums)
        self.getPreSum(right_min, right_max, nums[::-1])
        right_min.reverse()
        right_max.reverse()

        res = 0
        for i in range(n - 1):
            res = max(res, abs(left_max[i] - right_min[i + 1]), abs(right_max[i + 1] - left_min[i]))
        
        return res

    def getPreSum(self, mins, maxs, nums):
        cur = 0
        pre_sum_max = pre_sum_min = 0
        res_min, res_max = float('inf'), float('-inf')
        for i in range(len(nums)):
            cur += nums[i]
            
            res_max = max(res_max, cur - pre_sum_min)
            pre_sum_min = min(pre_sum_min, cur)
            maxs[i] = res_max
            
            res_min = min(res_min, cur - pre_sum_max)
            pre_sum_max = max(pre_sum_max, cur)
            mins[i] = res_min