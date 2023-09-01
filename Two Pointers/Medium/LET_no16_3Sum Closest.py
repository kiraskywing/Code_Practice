class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        res = sum(nums[:3])
        nums.sort()
        n = len(nums)
        
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            left, right = i + 1, n - 1
            while left < right:
                cur = nums[i] + nums[left] + nums[right]
                if cur == target:
                    return cur
                
                if abs(target - cur) < abs(target - res):
                    res = cur
                if cur < target:
                    left += 1
                else:
                    right -= 1
        
        return res
