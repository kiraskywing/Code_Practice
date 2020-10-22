class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        result = []
        for num in asteroids:
            if num > 0:
                result.append(num)
            else:
                while result and result[-1] > 0 and result[-1] < -num:
                    result.pop()
                if not result or result[-1] < 0:
                    result.append(num)
                elif result[-1] == -num:
                    result.pop()
        return result