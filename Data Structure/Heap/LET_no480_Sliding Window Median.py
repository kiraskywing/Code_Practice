class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        first, second = [], []
        for i in range(k):
            heapq.heappush(first, (-nums[i], i))
        for _ in range(k // 2):
            self.move(first, second)
            
        res = [self.getMedian(first, second, k)]
        for i in range(k, len(nums)):
            if nums[i] > -first[0][0]:
                heapq.heappush(second, (nums[i], i))
                if nums[i - k] <= second[0][0]:
                    self.move(second, first)
            else:
                heapq.heappush(first, (-nums[i], i))
                if nums[i - k] >= -first[0][0]:
                    self.move(first, second)

            """
            When nums[i - k] > -first[0][0], we add the new element to large.
            
            case 1. nums[i - k] < second[0][0]: we need to move one element from large to small to restablish initial lengths 
            (because large just got an element, but we know that small will lose one element soon).

            case 2. nums[i - k] == large[0][0]: we don't know if nums[i - k] is in small or in large, but the key is we don't care. 
            If nums[i - k] is actually in small, we need obviously to move one element from large to small. 
            But if nums[i - k] is in large, then it means the size of small and large are already OKAY, 
            but moving large[0][0] is also fine, large lose nothing, small gain nothing, the "real" lengths remain the same. 
            So it's always okay to move large[0] to small in case nums[i - k] == large[0][0]

            case 3. nums[i - k] > second[0][0]: the element to remove is inside large, but large just received one new element, 
            so we don"t need to do anything.
            """

            while first and first[0][1] <= i - k:
                heapq.heappop(first)
            while second and second[0][1] <= i - k:
                heapq.heappop(second)
            
            res.append(self.getMedian(first, second, k))
        
        return res
                    
    def move(self, heap1, heap2):
        val, i = heapq.heappop(heap1)
        heapq.heappush(heap2, (-val, i))
        
    def getMedian(self, first, second, k):
        if k % 2 != 0:
            return -first[0][0] * 1.0
        return (-first[0][0] + second[0][0]) / 2