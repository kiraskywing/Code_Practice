class Solution:
    """
    @param num: An integer
    @return: an integer array
    """

    def primeFactorization(self, num):

        upper_bound = int(num ** 0.5) + 1
        visited_f = [False] * upper_bound
        prime = []

        for i in range(2, upper_bound):
            if not visited_f[i]:
                prime.append(i)
                for j in range(i * i, upper_bound, i):
                    visited_f[j] = True

        result = []
        for a in prime:
            while num % a == 0:
                result.append(a)
                num //= a
        if num != 1:
            result.append(num)

        return result
