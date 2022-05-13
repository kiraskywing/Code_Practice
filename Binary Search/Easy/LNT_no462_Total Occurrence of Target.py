class Solution:
    """
    @param A: A an integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """
    def totalOccurrence(self, A, target):
        if not A:
            return 0
        
        first = self.findFirst(A, target)
        if first == -1:
            return 0
        
        last = self.findLast(A, target)
        return last - first + 1
    
    def findFirst(self, nums, target):
        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] >= target:
                right = mid
            else:
                left = mid
        if nums[left] == target:
            return left
        if nums[right] == target:
            return right
        return -1

    def findLast(self, nums, target):
        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] <= target:
                left = mid
            else:
                right = mid
        if nums[right] == target:
            return right
        return left


import bisect
class Solution2:
    """
    @param a: A an integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """
    def total_occurrence(self, a: List[int], target: int) -> int:
        left = bisect.bisect_left(a, target)
        right = bisect.bisect_right(a, target)
        
        if left == len(a) or a[left] != target:
            return 0
        return right - left