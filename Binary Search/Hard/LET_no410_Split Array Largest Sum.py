class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        left, right = max(nums), sum(nums)
        while left + 1 < right:
            mid = (left + right) // 2
            if self.count(nums, mid) > m:
                left = mid
            else:
                right = mid
        
        if self.count(nums, left) <= m:
            return left
        return right
    
    def count(self, nums, target):
        cnt = cur = 0
        for num in nums:
            if cur + num > target:
                cnt += 1
                cur = 0
            cur += num
        
        return cnt + 1