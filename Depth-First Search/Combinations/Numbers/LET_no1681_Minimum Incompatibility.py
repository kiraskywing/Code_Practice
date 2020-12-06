class Solution:
    def minimumIncompatibility(self, nums: List[int], k: int) -> int:
        if max(collections.Counter(nums).values()) > k:
            return -1
        
        nums.sort(reverse=True)
        upperbound = len(nums) // k
        arr = [[] for _ in range(k)]
        self.res = sys.maxsize
        self.helper(nums, arr, 0, k, upperbound)
        
        return self.res
    
    def helper(self, nums, arr, cur, k, upperbound):
        if cur == len(nums):
            self.res = min(self.res, sum((sub_arr[0] - sub_arr[-1]) for sub_arr in arr))
            return True
        
        flag = 0
        for i in range(k):
            if not arr[i] or (len(arr[i]) < upperbound and arr[i][-1] != nums[cur]):
                arr[i].append(nums[cur])
                if self.helper(nums, arr, cur + 1, k, upperbound): flag += 1
                arr[i].pop()
            
            if flag == 2:
                break
        return flag != 0
        