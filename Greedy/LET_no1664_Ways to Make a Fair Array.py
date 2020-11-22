class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        res = 0
        pre_sum, post_sum = [0, 0], [sum(nums[0::2]), sum(nums[1::2])]
        
        for i, num in enumerate(nums):
            post_sum[i % 2] -= num
            res += (pre_sum[0] + post_sum[1] == pre_sum[1] + post_sum[0])
            pre_sum[i % 2] += num
        
        return res