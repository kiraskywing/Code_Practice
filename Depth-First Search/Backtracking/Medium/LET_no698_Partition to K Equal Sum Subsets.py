class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0:
            return False
        
        target = total // k
        nums.sort(reverse=True)
        bk = [0] * k
        
        return self.helper(bk, nums, target, 0)
    
    def helper(self, bk, nums, target, i):
        if i == len(nums):
            if any(s != target for s in bk):
                return False
            return True
        
        for j in range(len(bk)):
            if bk[j] + nums[i] <= target:
                bk[j] += nums[i]
                if self.helper(bk, nums, target, i + 1):
                    return True
                bk[j] -= nums[i]
        
        return False