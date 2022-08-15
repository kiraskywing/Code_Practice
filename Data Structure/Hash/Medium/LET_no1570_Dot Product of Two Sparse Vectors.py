class SparseVector:
    def __init__(self, nums: List[int]):
        self.memo = {i:num for i, num in enumerate(nums) if num != 0}

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        res = 0
        for i, val in self.memo.items():
            if i in vec.memo:
                res += val * vec.memo[i]
        return res

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)