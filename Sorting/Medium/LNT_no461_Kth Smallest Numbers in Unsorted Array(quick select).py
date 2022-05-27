# Similar to LeetCode no215. Kth Largest Element in an Array

from random import randint

class Solution:
    """
    @param k: An integer
    @param nums: An integer array
    @return: kth smallest element
    """

    def kthSmallest(self, k, nums):
        return self.quickselect(nums, 0, len(nums) - 1, k - 1)
    
    def quickselect(self, nums, left, right, target):
        if left == right:
            return nums[left]
        
        pivot = nums[randint(left, right)]
        i, j = left, right
        while i <= j:
            while i <= j and nums[i] < pivot:
                i += 1
            while i <= j and nums[j] > pivot:
                j -= 1
            if i <= j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
                
        if target <= j:
            return self.quickselect(nums, left, j, target)
        elif target >= i:
            return self.quickselect(nums, i, right, target)
        return nums[target]