class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.extend([0, h])
        verticalCuts.extend([0, w])
        horizontalCuts.sort()
        verticalCuts.sort()
        diff_h = max(horizontalCuts[i + 1] - horizontalCuts[i] for i in range(len(horizontalCuts) - 1))
        diff_v = max(verticalCuts[i + 1] - verticalCuts[i] for i in range(len(verticalCuts) - 1))
        
        return (diff_h * diff_v) % (10 ** 9 + 7)