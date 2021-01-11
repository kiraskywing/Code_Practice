class Solution:
    def totalMoney(self, n: int) -> int:
        one_week = (1 + 7) * 7 // 2
        weeks = n // 7
        days = n % 7
        res = (one_week * 2 + 7 * (weeks - 1)) * weeks // 2 + (1 + weeks + days + weeks) * days // 2
        
        return res