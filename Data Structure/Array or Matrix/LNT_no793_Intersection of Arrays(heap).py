import heapq


class Solution:
    """
    @param arrs: the arrays
    @return: the number of the intersection of the arrays
    """

    def intersectionOfArrays(self, arrs):
        minheap = []
        for i in range(len(arrs)):
            if len(arrs[i]) == 0:
                return 0
            arrs[i].sort()
            heapq.heappush(minheap, (arrs[i][0], i, 0))

        last, count, result = None, 0, 0

        while minheap:
            cur, row, col = heapq.heappop(minheap)
            if last is None or cur != last or count == 0:
                if count == len(arrs):
                    result += 1
                last = cur
                count = 1
            else:
                count += 1

            if col + 1 < len(arrs[row]):
                heapq.heappush(minheap, (arrs[row][col + 1], row, col + 1))

        if count == len(arrs):
            result += 1

        return result
