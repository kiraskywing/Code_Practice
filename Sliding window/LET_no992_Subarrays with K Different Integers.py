class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:

        return self.at_most(A, K) - self.at_most(A, K - 1)

    def at_most(self, A, K):

        count = collections.Counter()
        res, i = 0, 0

        for j in range(len(A)):
            if count[A[j]] == 0:
                K -= 1

            count[A[j]] += 1

            while K < 0:
                count[A[i]] -= 1
                if count[A[i]] == 0:
                    K += 1
                i += 1

            res += j - i + 1

        return res
