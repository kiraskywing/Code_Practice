# The same as LeetCode no50. Pow(x, n)

class Solution:
    """
    @param x {float}: the base number
    @param n {int}: the power number
    @return {float}: the result
    """

    def myPow(self, x, n):

        if n < 0:
            x = 1 / x
            n = -n

        ans = 1
        temp = x

        while n > 0:

            if n % 2 != 0:
                ans *= temp

            temp *= temp
            n //= 2

        return ans