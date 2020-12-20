class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        dp = [0] * len(nums)
        dp[0] = nums[0]
        queue = collections.deque([(0, nums[0])])
        
        for i in range(1, len(nums)):
            dp[i] = queue[0][1] + nums[i]
            while queue and queue[-1][1] < dp[i]:
                queue.pop()
            
            queue.append((i, dp[i]))
            if queue[0][0] == i - k:
                queue.popleft()
        
        return dp[-1]