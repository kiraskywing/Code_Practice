class Solution:
    """
    @param n: a number represent year
    @return: whether year n is a leap year.
    """
    def isLeapYear(self, n):
        return n % 400 == 0 or n % 4 == 0 and n % 100 != 0

if __name__ == '__main__':
    res = Solution()
    print(res.isLeapYear(2016))
