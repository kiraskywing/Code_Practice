class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        temp = [0] * len(nums)
        self.mergeSort(nums, temp, 0, len(nums) - 1)
        return nums
    
    def mergeSort(self, nums, temp, left, right):
        if left >= right:
            return
        
        mid = (left + right) // 2
        self.mergeSort(nums, temp, left, mid)
        self.mergeSort(nums, temp, mid + 1, right)
        self.helper(nums, temp, left, right)
        
    def helper(self, nums, temp, left, right):
        mid = (left + right) // 2
        i, j, k = left, mid + 1, left
        while i <= mid and j <= right:
            if nums[i] < nums[j]:
                temp[k] = nums[i]
                i += 1
            else:
                temp[k] = nums[j]
                j += 1
            k += 1
        
        while i <= mid:
            temp[k] = nums[i]
            i += 1
            k += 1
        while j <= right:
            temp[k] = nums[j]
            j += 1
            k += 1
            
        nums[left:right+1] = temp[left:right+1]    