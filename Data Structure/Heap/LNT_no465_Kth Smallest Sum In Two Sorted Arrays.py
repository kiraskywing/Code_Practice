import heapq

class Solution:
    """
    @param A: an integer arrays sorted in ascending order
    @param B: an integer arrays sorted in ascending order
    @param k: An integer
    @return: An integer
    """
    def kthSmallestSum(self, A, B, k):
        m, n = len(A), len(B)
        temp = [(A[0] + B[0], 0, 0)]
        visited = set([0])

        res = 0
        for _ in range(k):
            res, i, j = heapq.heappop(temp)
            if i + 1 < m and (i + 1) * n + j not in visited:
                visited.add((i + 1) * n + j)
                heapq.heappush(temp, (A[i + 1] + B[j], i + 1, j))
            if j + 1 < n and i * n + j + 1 not in visited:
                visited.add(i * n + j + 1)
                heapq.heappush(temp, (A[i] + B[j + 1], i, j + 1))
        
        return res
