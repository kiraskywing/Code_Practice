class Solution:
    def countRectangles(self, rectangles: List[List[int]], points: List[List[int]]) -> List[int]:
        rectangles.sort()
        memo = collections.defaultdict(list)
        for width, height in rectangles:
            memo[height].append(width)
            
        res = []
        for x, y in points:
            res.append(self.helper(memo, x, y))
        return res
    
    def helper(self, memo, x, y):
        count = 0
        for height, widths in memo.items():
            if height >= y:
                count += len(widths) - bisect.bisect(widths, x - 1)
        return count