class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums
        
        queue = collections.deque()
        res = []
        
        for i in range(k):
            while queue and nums[i] > nums[queue[-1]]:
                queue.pop()
            queue.append(i)
                    
        
        for i in range(k, len(nums)):
            res.append(nums[queue[0]])
            
            if queue[0] < i - k + 1:
                queue.popleft()
            
            while queue and nums[i] > nums[queue[-1]]:
                queue.pop()
            queue.append(i)
        
        res.append(nums[queue[0]])
        
        return res