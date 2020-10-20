class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        countA, countB, same = [0] * 7, [0] * 7, [0] * 7
        n = len(A)
        for i in range(n):
            countA[A[i]] += 1
            countB[B[i]] += 1
            if A[i] == B[i]: same[A[i]] += 1
        
        for i in range(1, 7):
            if countA[i] + countB[i] - same[i] == n:
                return n - max(countA[i], countB[i])
        
        return -1