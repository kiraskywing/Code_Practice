class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        array = [0] * arrLen
        array[0] = 1
        mod = 10 ** 9 + 7

        for i in range(steps):
            temp = [0] * arrLen
            for j in range(min(arrLen, steps - i)):
                temp[j] = array[j] % mod
                if j - 1 >= 0:
                    temp[j] += array[j - 1] % mod
                if j + 1 < arrLen:
                    temp[j] += array[j + 1] % mod
            array = temp

        return array[0] % mod