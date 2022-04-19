class Solution:
    """
    @param: A: An integer array
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def continuousSubarraySumII(self, A):
        max_start, max_end, max_value = self.findMaxSubarraySum(A)
        min_start, min_end, min_value = self.findMaxSubarraySum([-num for num in A])
        min_value = -min_value
        total = sum(A)
        
        if max_value >= total - min_value or min_end - min_start + 1 == len(A):
            return [max_start, max_end]
        return [min_end + 1, min_start - 1]

    def findMaxSubarraySum(self, nums):
        max_sum = float('-inf')
        cur, start = 0, 0
        indices = []
        for i, num in enumerate(nums):
            if cur < 0:
                cur = 0
                start = i
            cur += num
            if cur > max_sum:
                max_sum = cur
                indices = [start, i]
        
        return indices[0], indices[1], max_sum