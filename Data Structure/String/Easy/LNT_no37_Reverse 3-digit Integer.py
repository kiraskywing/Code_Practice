class Solution:
    """
    @param number: A 3-digit number.
    @return: Reversed number.
    """
    def reverseInteger(self, number):
        return int(str(number)[::-1])

        """
        Solution 2
        return number % 10 * 100 + number / 10 % 10 * 10 + number / 100
        """



if __name__ == '__main__':
    sol = Solution()
    print(sol.reverseInteger(32001))