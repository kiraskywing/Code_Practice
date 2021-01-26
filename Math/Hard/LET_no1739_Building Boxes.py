class Solution:
    def minimumBoxes(self, n: int) -> int:
        x = int((6 * n) ** (1 / 3))
        if x * (x + 1) * (x + 2) > 6 * n: x -= 1
        n -= x * (x + 1) * (x + 2) // 6
        y = int((2 * n) ** (1 / 2))
        if y * (y + 1) < 2 * n: y += 1
        return x * (x+1) // 2 + y