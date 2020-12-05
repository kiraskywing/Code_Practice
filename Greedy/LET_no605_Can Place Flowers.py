class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        n = len(flowerbed)
        for i in range(n):
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i - 1] == 0) and (i == n - 1 or flowerbed[i + 1] == 0):
                flowerbed[i] = 1
                n -= 1
                if n == 0:
                    return True
        print(flowerbed, n)
        return False