class Solution:
    def maximumSwap(self, num: int) -> int:
        num = list(str(num))
        n = len(num)
        
        max_i = n - 1
        i1 = i2 = 0
        for i in range(n - 1, -1, -1):
            if num[i] > num[max_i]:
                max_i = i
            elif num[i] < num[max_i]:
                i1, i2 = i, max_i
        
        num[i1], num[i2] = num[i2], num[i1]
        
        return int(''.join(num))