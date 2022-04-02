# The same as LeetCode no680. Valid Palindrome II

class Solution:
    """
    @param s: a string
    @return bool: whether you can make s a palindrome by deleting at most one character
    """

    def validPalindrome(self, s):
        left, right = self.scan_string(s, 0, len(s) - 1)
        if left >= right:
            return True

        return self.is_Palindrome(s, left + 1, right) or self.is_Palindrome(s, left, right - 1)

    def scan_string(self, string, left, right):
        while left < right:
            if string[left] != string[right]:
                return left, right
            left += 1
            right -= 1
        return left, right

    def is_Palindrome(self, string, left, right):
        left, right = self.scan_string(string, left, right)
        return left >= right