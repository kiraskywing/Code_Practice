class Solution:
    """
    @param num: An integer
    @return: an integer array
    """

    def primeFactorization(self, num):
        res = []
        up = int(num ** 0.5) + 1
        for i in range(2, up):
            while num % i == 0:
                res.append(i)
                num //= i
        if num > 1:
            res.append(num)

        return res
