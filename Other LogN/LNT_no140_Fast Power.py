class Solution:
    """
    @param a: A 32bit integer
    @param b: A 32bit integer
    @param n: A 32bit integer
    @return: An integer
    """

    def fastPower(self, a, b, n):

        ans = 1

        while n > 0:

            if n % 2 != 0:
                ans = (ans * a) % b

            a = (a * a) % b
            n //= 2

        return ans % b  # a = 3, b = 1, n = 0