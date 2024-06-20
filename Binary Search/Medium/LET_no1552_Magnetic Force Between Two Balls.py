class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        left, right = 0, position[-1] - position[0]
        while left + 1 < right:
            mid = (left + right) // 2
            if self.helper(mid, position) >= m:
                left = mid
            else:
                right = mid

        if self.helper(right, position) >= m:
            return right
        return left

    def helper(self, least_dist, pos):
        res = 1
        prev_pos = pos[0]
        for i in range(1, len(pos)):
            if pos[i] - prev_pos >= least_dist:
                res += 1
                prev_pos = pos[i]
        
        return res