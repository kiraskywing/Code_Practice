class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            cur = abs(nums[i])
            if nums[cur] < 0:
                return cur
            
            nums[cur] = -nums[cur]
            
        return 0
            
# without modification
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = nums[0], nums[nums[0]]
        while slow != fast:
            slow, fast = nums[slow], nums[nums[fast]]
        
        fast = 0
        while slow != fast:
            slow, fast = nums[slow], nums[fast]
        
        return slow