# the same as LeetCode no7. Reverse Integer

class Solution:
    """
    @param n: the integer to be reversed
    @return: the reversed integer
    """
    def reverseInteger(self, n):

        if n == 0:
            return 0

        neg = 1
        if n < 0:
            neg, n = -1, -n

        res = 0
        while n > 0:
            res = res * 10 + n % 10
            n //= 10

        res = res * neg

        if res < -(2 ** 31) or res > 2 ** 31 - 1:
            return 0
        else:
            return res

        """
        if n < 0:
            a = 0 - int(str(n)[-1:0:-1])
            if a > 0 - 2 ** 32:
                return a
            else:
                return 0

        else:
            a = int(str(n)[::-1])
            if a < 2 ** 32:
                return a
            else:
                return 0
        """