class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        target = self.quickSelect(nums, 0, len(nums) - 1, len(nums) // 2)
        return sum(abs(num - target) for num in nums)
    
    def quickSelect(self, nums, left, right, k):
        if left == right:
            return nums[left]
        
        pivot = nums[random.randint(left, right)]
        i, j = left, right
        while i <= j:
            while i <= j and nums[i] < pivot:
                i += 1
            while i <= j and pivot < nums[j]:
                j -= 1
            if i <= j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
        
        if k <= j:
            return self.quickSelect(nums, left, j, k)
        if k >= i:
            return self.quickSelect(nums, i, right, k)
        return nums[k]