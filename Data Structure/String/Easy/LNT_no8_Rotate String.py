from typing import (
    List,
)

class Solution:
    """
    @param str: An array of char
    @param offset: An integer
    @return: nothing
    """
    def rotateString(self, str: List[str], offset: int):
        if not str:
            return str

        n = len(str)
        offset %= n
        self.reverse(str, 0, n - offset - 1)
        self.reverse(str, n - offset, n - 1)
        self.reverse(str, 0, n - 1)
        return str
    
    def reverse(self, s, left, right):
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1