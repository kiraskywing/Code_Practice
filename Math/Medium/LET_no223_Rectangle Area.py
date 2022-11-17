class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        area_a = (ay2 - ay1) * (ax2 - ax1)
        area_b = (by2 - by1) * (bx2 - bx1)
        res = area_a + area_b
        
        cx1, cy1 = max(ax1, bx1), max(ay1, by1)
        cx2, cy2 = min(ax2, bx2), min(ay2, by2)
        
        if cx1 <= cx2 and cy1 <= cy2:
            res -= (cx2 - cx1) * (cy2 - cy1)
        
        return res