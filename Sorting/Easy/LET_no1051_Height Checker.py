class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sorted_heights = sorted(heights)
        res = 0
        for i in range(len(heights)):
            res += sorted_heights[i] != heights[i]
        
        return res