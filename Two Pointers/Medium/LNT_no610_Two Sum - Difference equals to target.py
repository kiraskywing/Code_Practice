class Solution:
    """
    @param nums: an array of Integer
    @param target: an integer
    @return: [num1, num2] (num1 < num2)
    """
    def twoSum7(self, nums, target):
        n = len(nums)
        if n < 2:
            return []
        
        target = abs(target)
        left, right = 0, 1
        while right < n:
            if nums[right] - nums[left] == target:
                return [nums[left], nums[right]]
            while right < n and nums[right] - nums[left] < target:
                right += 1
            while right < n and left < right and nums[right] - nums[left] > target:
                left += 1
                if left == right:
                    right += 1
        return []