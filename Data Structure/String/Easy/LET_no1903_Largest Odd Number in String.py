class Solution:
    def largestOddNumber(self, num: str) -> str:
        i = len(num) - 1
        while int(num[i]) % 2 == 0 and i >= 0:
            i -= 1
        
        return num[:i + 1] if i >= 0 else ""