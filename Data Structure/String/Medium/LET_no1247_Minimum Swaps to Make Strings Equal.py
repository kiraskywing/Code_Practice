class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:

        s1_x, s1_y = 0, 0

        for i in range(len(s1)):
            if s1[i] != s2[i] and s1[i] == "x":
                s1_x += 1
            if s1[i] != s2[i] and s1[i] == "y":
                s1_y += 1

        if (s1_x + s1_y) % 2 != 0:
            return -1

        return s1_x // 2 + s1_y // 2 + 2 * (s1_x % 2)