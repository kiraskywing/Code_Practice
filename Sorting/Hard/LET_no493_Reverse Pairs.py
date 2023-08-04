class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        temp = [0] * len(nums)
        return self.helper(nums, temp, 0, len(nums) - 1)

    def helper(self, nums, temp, left, right):
        if left >= right:
            return 0

        mid = (left + right) // 2
        return self.helper(nums, temp, left, mid) + \
               self.helper(nums, temp, mid + 1, right) + \
               self.merger(nums, temp, left, right)

    def merger(self, nums, temp, left, right):
        mid = (left + right) // 2
        i, j, k, z = left, mid + 1, left, mid + 1
        res = 0
        
        while i <= mid:
            while z <= right and nums[i] > nums[z] * 2:
                z += 1
            res += z - (mid + 1)

            while j <= right and nums[i] >= nums[j]:
                temp[k] = nums[j]
                k += 1
                j += 1
            
            temp[k] = nums[i]
            k += 1
            i += 1

        while j <= right:
            temp[k] = nums[j]
            k += 1
            j += 1

        for idx in range(left, right + 1):
            nums[idx] = temp[idx]
        
        return res