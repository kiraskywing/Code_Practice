class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = collections.deque([])
        for i in range(k):
            while queue and nums[queue[-1]] <= nums[i]:
                queue.pop()
            queue.append(i)
        
        res = [nums[queue[0]]]
        for i in range(k, len(nums)):
            if queue[0] <= i - k:
                queue.popleft()
            while queue and nums[queue[-1]] <= nums[i]:
                queue.pop()
            queue.append(i)
            res.append(nums[queue[0]])
        
        return res

class Solution2:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = []
        for i in range(k):
            heapq.heappush(window, (-nums[i], i))
            
        res = [-window[0][0]]
        for i in range(k, len(nums)):
            heapq.heappush(window, (-nums[i], i))
            while window and window[0][1] <= i - k:
                heapq.heappop(window)
                
            res.append(-window[0][0])
        
        return res