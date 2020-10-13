class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        mark, count = 1, 0

        while mark <= a or mark <= b or mark <= c:
            if mark & c == 0:
                if mark & a != 0:
                    count += 1
                if mark & b != 0:
                    count += 1
            else:
                if mark & a == 0 and mark & b == 0:
                    count += 1
            mark <<= 1

        return count