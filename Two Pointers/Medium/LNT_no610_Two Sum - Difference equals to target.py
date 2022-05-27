class Solution:
    """
    @param nums: an array of Integer
    @param target: an integer
    @return: [num1, num2] (num1 < num2)
    """
    def twoSum7(self, nums, target):
        left, right = 0, 1
        n = len(nums)
        target = abs(target)
        
        while right < n:
            if nums[right] - nums[left] == target:
                return [nums[left], nums[right]]
            elif nums[right] - nums[left] < target:
                right += 1
            else:
                if left + 1 < right:
                    left += 1
                else:
                    right += 1
        
        return []