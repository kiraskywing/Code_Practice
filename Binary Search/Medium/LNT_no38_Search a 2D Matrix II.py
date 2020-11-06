class Solution:
    """
    @param matrix: A list of lists of integers
    @param target: An integer you want to search in matrix
    @return: An integer indicate the total occurrence of target in the given matrix
    """

    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0] or target is None:
            return 0

        result = 0
        for i in range(len(matrix)):
            result += self.counter(matrix[i], target)
        return result

    def counter(self, nums, target):
        left, right = 0, len(nums) - 1

        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid
            else:
                right = mid

        if nums[left] == target:
            head = left
        elif nums[right] == target:
            head = right
        else:
            return 0

        left, right = head, len(nums) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] <= target:
                left = mid
            else:
                right = mid

        if nums[right] == target:
            tail = right
        elif nums[left] == target:
            tail = left

        return tail - head + 1
