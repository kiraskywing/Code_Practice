class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        record = set()
        for i in range(int(sqrt(c)) + 1):
            record.add(i * i)
            if c - i * i in record:
                return True
        return False