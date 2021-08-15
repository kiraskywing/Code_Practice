class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        @cache
        def dp(left, right, k):
            if left > right:
                return 0
            while left + 1 <= right and boxes[left] == boxes[left + 1]:
                left += 1
                k += 1
            res = (k + 1) * (k + 1) + dp(left + 1, right, 0)
            
            for i in range(left + 1, right + 1):
                if boxes[i] == boxes[left]:
                    res = max(res, dp(left + 1, i - 1, 0) + dp(i, right, k + 1))
            
            return res
        
        return dp(0, len(boxes) - 1, 0)