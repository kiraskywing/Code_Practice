# The same as LeetCode no204. Count Primes

class Solution:
    """
    @param n: a integer
    @return: return a integer
    """

    def countPrimes(self, n):

        if n < 3:
            return 0

        is_prime = [True] * n
        is_prime[0] = is_prime[1] = False

        for num in range(2, int(n ** 0.5) + 1):
            if is_prime[num]:
                for num2 in range(num * num, n, num):
                    is_prime[num2] = False

        return sum(is_prime)