class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        record, res = [0] * 46, 0
        for num in range(lowLimit, highLimit + 1):
            key = 0
            while num > 0:
                key += num % 10
                num //= 10
            record[key] += 1
            res = max(res, record[key])
        return res