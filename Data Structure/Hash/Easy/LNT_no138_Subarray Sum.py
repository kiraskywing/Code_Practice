class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def subarraySum(self, nums):
        memo = {0: -1}
        prefix_sum = 0
        for i, num in enumerate(nums):
            prefix_sum += num
            if prefix_sum in memo:
                return [memo[prefix_sum] + 1, i]
            memo[prefix_sum] = i
        
        return [-1, -1]