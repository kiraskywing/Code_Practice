class Solution:
    def isHappy(self, n: int) -> bool:
        memo = set()
        while n != 1 or n != 0:
            cur = 0
            while n > 0:
                cur += (n % 10) ** 2
                n //= 10
            n = cur
            if n in memo:
                break
            memo.add(n)
            
        return n == 1