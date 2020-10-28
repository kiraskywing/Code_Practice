class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        res = []
        for i, j in zip(l, r):
            res.append(self.helper(nums[i : j + 1]))
        return res
    
    def helper(self, arr):
        max_val, min_val, temp = max(arr), min(arr), set(arr)
        
        if (max_val - min_val) % (len(arr) - 1) != 0: return False
        
        step = (max_val - min_val) // (len(arr) - 1)
        if step == 0: return max_val == min_val
        
        for i in range(min_val, max_val, step):
            if i not in temp: return False
        
        return True