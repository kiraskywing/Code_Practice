class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        i, j, di, dj = 0, 0, 0, 1
        for c in instructions:
            if c == 'R': 
                di, dj = dj, -di
            if c == 'L':
                di, dj = -dj, di
            if c == 'G':
                i, j = i + di, j + dj
        return (i, j) == (0, 0) or (di, dj) != (0, 1)