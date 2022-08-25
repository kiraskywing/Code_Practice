class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        m, n = len(nums1), len(nums2)
        if m > n:
            return self.intersect(nums2, nums1)
        
        memo = collections.Counter(nums1)
        res = []
        for num in nums2:
            if memo[num] > 0:
                res.append(num)
                memo[num] -= 1
        
        return res