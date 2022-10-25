class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        memo = collections.defaultdict(int)
        for num in nums[:k + 1]:
            memo[num] += 1
            if memo[num] > 1:
                return True
            
        left = 0
        for right in range(k + 1, len(nums)):
            memo[nums[left]] -= 1
            left += 1
            memo[nums[right]] += 1
            if memo[nums[right]] > 1:
                return True
        
        return False