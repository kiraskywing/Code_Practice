class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if t < 0 or not nums or k <= 0:
            return False
        bucket = {}
        width = t + 1
        
        for i, num in enumerate(nums):
            buck = num // width
            if buck in bucket:
                return True
            
            bucket[buck] = num
            if buck - 1 in bucket and num - bucket[buck - 1] <= t:
                return True
            if buck + 1 in bucket and bucket[buck + 1] - num <= t:
                return True
            if i >= k:
                del bucket[nums[i - k] // width]
        
        return False