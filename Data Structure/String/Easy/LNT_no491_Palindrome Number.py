class Solution:
    """
    @param num: a positive number
    @return: true if it's a palindrome or false
    """
    def isPalindrome(self, num):
        n = str(num)
        return n == n[::-1]

        """
        ans, temp = 0, num

        while temp != 0:
            ans = ans * 10 + temp % 10
            temp //= 10

        return ans == num
        """