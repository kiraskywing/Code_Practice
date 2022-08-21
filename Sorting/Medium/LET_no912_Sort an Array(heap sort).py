class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.buildMaxHeap(nums)
        self.sortHelper(nums)
        return nums
            
    def buildMaxHeap(self, nums):
        for i in range(len(nums) // 2 - 1, -1, -1):
            self.maxHeapify(nums, i, len(nums))
            
    def maxHeapify(self, nums, parent, size):
        while True:
            child = parent * 2 + 1
            if child >= size:
                break
            if child + 1 < size and nums[child + 1] > nums[child]:
                child += 1
            if nums[child] > nums[parent]:
                nums[child], nums[parent] = nums[parent], nums[child]
                parent = child
            else:
                break
                
    def sortHelper(self, nums):
        n = len(nums)
        for i in range(len(nums) - 1, 0, -1):
            nums[0], nums[i] = nums[i], nums[0]
            n -= 1
            self.maxHeapify(nums, 0, n)