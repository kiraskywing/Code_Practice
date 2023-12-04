class Solution:
    def largestGoodInteger(self, num: str) -> str:
        n = len(num)
        res = -1
        for i in range(2, n):
            if num[i - 2] == num[i - 1] == num[i] and int(num[i]) > res:
                res = int(num[i])
        
        return "" if res == -1 else str(res) * 3
