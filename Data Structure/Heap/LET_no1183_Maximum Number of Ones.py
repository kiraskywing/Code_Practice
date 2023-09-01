class Solution:
    def maximumNumberOfOnes(self, width: int, height: int, sideLength: int, maxOnes: int) -> int:
        memo = [[0 for _ in range(sideLength)] for _ in range(sideLength)]
        
        for i in range(height):
            for j in range(width):
                memo[i % sideLength][j % sideLength] += 1
        
        pq = []
        for i in range(sideLength):
            for j in range(sideLength):
                heapq.heappush(pq, -memo[i][j])
        
        res = 0
        for _ in range(maxOnes):
            res += -heapq.heappop(pq)
        
        return res