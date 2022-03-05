from typing import (
    List,
)

import heapq

class Solution:
    """
    @param arrays: a list of array
    @param k: An integer
    @return: an integer, K-th largest element in N arrays
    """
    def kth_in_arrays(self, arrays: List[List[int]], k: int) -> int:
        temp = []
        for i in range(len(arrays)):
            if arrays[i]:
                arrays[i].sort(reverse=True)
                heapq.heappush(temp, (-arrays[i][0], i, 0))
        
        res = 0
        for _ in range(k):
            res, i, j = heapq.heappop(temp)
            if j + 1 < len(arrays[i]):
                heapq.heappush(temp, (-arrays[i][j + + 1], i, j + 1))
        return -res
