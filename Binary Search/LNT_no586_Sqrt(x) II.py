class Solution:
    """
    @param x: a double
    @return: the square root of x
    """

    def sqrt(self, x):
        if x >= 1:
            start, end = 1, x
        else:
            start, end = x, 1

        while end - start > 1e-10:
            mid = (start + end) / 2
            if mid * mid <= x:
                start = mid
            else:
                end = mid
        return start