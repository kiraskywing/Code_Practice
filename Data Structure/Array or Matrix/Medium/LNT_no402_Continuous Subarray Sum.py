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

class Solution2:
    """
    @param a: An integer array
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def continuous_subarray_sum(self, a: List[int]) -> List[int]:
        res = a[0]
        left = right = 0
        cur = a[0]

        i = 0
        for j in range(1, len(a)):
            cur += a[j]
            if a[j] > cur:
                cur = a[j]
                i = j
            if cur > res:
                res = cur
                left, right = i, j
        
        return [left, right]