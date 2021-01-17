class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        res = count = 0
        for l1, l2 in rectangles:
            cur = min(l1, l2)
            if cur > res:
                res, count = cur, 1
            elif cur == res:
                count += 1
        return count