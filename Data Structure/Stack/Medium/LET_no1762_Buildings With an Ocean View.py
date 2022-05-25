class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        res = []
        for i in range(len(heights) - 1, -1, -1):
            if not res or heights[i] > heights[res[-1]]:
                res.append(i)
        
        res.reverse()
        return res