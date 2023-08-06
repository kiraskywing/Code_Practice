from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if all(num == 0 for num in nums):
            return "0"

        n = len(nums)
        temp = ["0" for _ in range(n)]
        nums = [str(num) for num in nums]
        self.helper(nums, temp, 0, n - 1)
        return ''.join(nums)

    def helper(self, nums, temp, left, right):
        if left >= right:
            return 

        mid = (left + right) // 2
        self.helper(nums, temp, left, mid)
        self.helper(nums, temp, mid + 1, right)
        self.merger(nums, temp, left, right)

    def merger(self, nums, temp, left, right):
        mid = (left + right) // 2
        i, j, k = left, mid + 1, left

        while i <= mid and j <= right:
            if nums[i] + nums[j] > nums[j] + nums[i]:
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
        
        for idx in range(left, right + 1):
            nums[idx] = temp[idx]

        """
        nums.sort(key=cmp_to_key(lambda x, y: 1 if str(x) + str(y) < str(y) + str(x) else -1))

        if nums[0] == 0:
            return '0'

        return "".join([str(x) for x in nums])
        """