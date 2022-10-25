class Solution:
    def countEven(self, num: int) -> int:
        res = 0
        for i in range(1, num + 1):
            odd = 0
            for d in str(i):
                odd += int(d) % 2 != 0
            res += odd % 2 == 0
        
        return res