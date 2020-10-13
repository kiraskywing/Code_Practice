import heapq


class Solution:
    """
    @param n: An integer
    @return: return a  integer as description.
    """

    def nthUglyNumber(self, n):
        heap = [1]
        visited = set([1])
        val = None

        for _ in range(n):
            val = heapq.heappop(heap)
            for factor in [2, 3, 5]:
                if val * factor not in visited:
                    visited.add(val * factor)
                    heapq.heappush(heap, val * factor)

        return val
