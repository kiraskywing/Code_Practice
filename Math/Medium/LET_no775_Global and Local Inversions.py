class Solution:
    def isIdealPermutation(self, A: List[int]) -> bool:
        cur_max = 0
        for i in range(len(A) - 2):
            cur_max = max(cur_max, A[i])
            if cur_max > A[i + 2]: return False
        return True