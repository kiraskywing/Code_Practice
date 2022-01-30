class Solution:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        n = len(A)
        pos_A = [(x, y) for x in range(n) for y in range(n) if A[x][y] == 1]
        pos_B = [(x, y) for x in range(n) for y in range(n) if B[x][y] == 1]
        
        count = collections.defaultdict(int)
        for i, j in pos_A:
            for i2, j2 in pos_B:
                count[(i - i2, j - j2)] += 1
        return max(count.values() or [0])