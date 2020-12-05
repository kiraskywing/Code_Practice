class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        factors = []
        for i in range(1, int(n ** 0.5) + 1):
            if n % i == 0:
                if i ** 2 != n:
                    factors.append(i)
                k -= 1
                if k == 0:
                    return i
        
        return -1 if k > len(factors) else n // factors[-k]