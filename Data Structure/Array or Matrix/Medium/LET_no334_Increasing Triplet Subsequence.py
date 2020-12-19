class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False
        min_val, mid_val = float('inf'), float('inf')
        for n in nums:
            if n <= min_val:
                min_val = n
            elif n <= mid_val:
                mid_val = n
            else:
                return True
        
        return False