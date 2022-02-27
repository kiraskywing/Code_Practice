from typing import (
    List,
)

class Solution:
    """
    @param nums: A list of integers
    @param k: An integer denote to find k non-overlapping subarrays
    @return: An integer denote the sum of max k non-overlapping subarrays
    """
    def max_sub_array(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if n < k:
            return 0

        must_choose_cur = [[float('-inf') for _ in range(k + 1)] for _ in range(n + 1)]
        may_not_choose_cur = [[float('-inf') for _ in range(k + 1)] for _ in range(n + 1)]

        for n_nums in range(n + 1):
            must_choose_cur[n_nums][0] = 0
            may_not_choose_cur[n_nums][0] = 0
            for n_groups in range(1, min(n_nums + 1, k + 1)):
                must_choose_cur[n_nums][n_groups] = max(
                    must_choose_cur[n_nums - 1][n_groups] + nums[n_nums - 1],
                    must_choose_cur[n_nums - 1][n_groups - 1] + nums[n_nums - 1],
                    may_not_choose_cur[n_nums - 1][n_groups - 1] + nums[n_nums - 1]
                )
                
                may_not_choose_cur[n_nums][n_groups] = max(
                    must_choose_cur[n_nums][n_groups], 
                    may_not_choose_cur[n_nums - 1][n_groups]
                )

        return max(must_choose_cur[-1][-1], may_not_choose_cur[-1][-1])
