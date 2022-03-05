class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        points = [0] * (10001)
        for num in nums:
            points[num] += num
        
        take = skip = 0
        for i in range(10001):
            take_i = skip + points[i]
            skip_i = max(take, skip)
            take, skip = take_i, skip_i
        
        return max(take, skip)