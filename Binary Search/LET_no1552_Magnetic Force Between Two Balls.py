class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        self.n = len(position)
        position.sort()
        
        left, right = 0, position[-1] - position[0]
        while left + 1 < right:
            mid = (left + right) // 2
            if self.count(mid, position) >= m:
                left = mid
            else:
                right = mid
        
        if self.count(right, position) == m:
            return right
        
        return left
        
        
    def count(self, d, position):
        ans, cur = 1, position[0]
        for i in range(1, self.n):
            if position[i] - cur >= d:
                ans += 1
                cur = position[i]
        return ans