class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        left, right = 0, n - 1
        for i in range(n - 1, -1, -1):
            if abs(nums[right]) > abs(nums[left]):
                res[i] = nums[right] ** 2
                right -= 1
            else:
                res[i] = nums[left] ** 2
                left += 1
        
        return res

        # Solution 2
        return sorted(x ** 2 for x in nums)