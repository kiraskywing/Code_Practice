from typing import (
    List,
)

import heapq

class Solution:
    """
    @param arrs: the arrays
    @return: the number of the intersection of the arrays
    """
    def intersection_of_arrays(self, arrs: List[List[int]]) -> int:
        temp = []
        m = len(arrs)
        
        for i in range(m):
            if not arrs[i]:
                return 0
            arrs[i].sort()
            heapq.heappush(temp, (arrs[i][0], i, 0))

        res, count, last = 0, 0, None
        while temp:
            cur, i, j = heapq.heappop(temp)
            if not last or last != cur:
                last = cur
                count = 1
            elif cur == last:
                count += 1
                if count == m:
                    res += 1
            
            if j + 1 < len(arrs[i]):
                heapq.heappush(temp, (arrs[i][j + 1], i, j + 1))

        return res