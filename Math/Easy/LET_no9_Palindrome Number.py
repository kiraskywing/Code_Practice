class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        temp = x
        copy = 0
        while temp:
            copy = copy * 10 + temp % 10
            temp //= 10
        return copy == x