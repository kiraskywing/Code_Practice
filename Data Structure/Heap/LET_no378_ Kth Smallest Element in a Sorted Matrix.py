class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []
        for i in range(min(k, len(matrix))):
            heapq.heappush(heap, (matrix[i][0], i, 0))
            
        res = None
        for _ in range(k):
            cur, i, j = heapq.heappop(heap)
            res = cur
            if j + 1 < len(matrix[i]):
                heapq.heappush(heap, (matrix[i][j + 1], i, j + 1))
                
        return res