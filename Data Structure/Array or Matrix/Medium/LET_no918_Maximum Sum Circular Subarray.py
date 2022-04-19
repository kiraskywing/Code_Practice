class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total, cur_max, max_sum, cur_min, min_sum = 0, 0, float('-inf'), 0, float('inf')
        for num in nums:
            cur_max = max(cur_max + num, num)
            max_sum = max(max_sum, cur_max)
            cur_min = min(cur_min + num, num)
            min_sum = min(min_sum, cur_min)
            total += num
        return max(max_sum, total - min_sum) if min_sum != total else max_sum