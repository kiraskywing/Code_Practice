from typing import (
    List,
)

class Solution:
    """
    @param a: An integer array
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def continuous_subarray_sum(self, a: List[int]) -> List[int]:
        n = len(a)
        first, second = 0, 0
        pre_sum, pre_min, min_i = 0, 0, -1
        pre_max = float('-inf')
        
        for i, num in enumerate(a):
            pre_sum += num
            if pre_sum - pre_min > pre_max:
                pre_max = pre_sum - pre_min
                first, second = min_i + 1, i
            if pre_sum < pre_min:
                pre_min = pre_sum
                min_i = i
        
        return [first, second]