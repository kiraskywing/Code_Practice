class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        size = len(flowerbed)
        for i in range(size):
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i - 1] == 0) and (i == size - 1 or flowerbed[i + 1] == 0):
                n -= 1
                flowerbed[i] = 1
                if n == 0:
                    return True
        return False