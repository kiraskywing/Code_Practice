class Solution:
    def addDigits(self, num: int) -> int:
        while num // 10:
            cur = 0
            while num:
                cur += num % 10
                num //= 10
            num = cur
        return num
    
        return 1 + (num - 1) % 9 if num else 0