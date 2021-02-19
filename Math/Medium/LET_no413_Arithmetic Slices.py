class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        if len(A) < 3:
            return 0
        
        res = cur = 0
        for i in range(2, len(A)):
            if A[i] - A[i - 1] != A[i - 1] - A[i - 2]:
                cur = 0
            else:
                cur += 1
                res += cur
        
        return res