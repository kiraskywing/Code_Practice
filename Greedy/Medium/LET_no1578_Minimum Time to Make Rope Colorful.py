class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        n = len(colors)
        res = 0
        left = 0
        
        while left < n:
            right = left
            total = 0
            max_val = neededTime[left]
            while right < n and colors[right] == colors[left]:
                total += neededTime[right]
                max_val = max(max_val, neededTime[right])
                right += 1
                
            res += total - max_val
            left = right
        
        return res