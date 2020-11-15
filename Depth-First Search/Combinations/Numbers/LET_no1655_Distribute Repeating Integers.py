class Solution:
    def canDistribute(self, nums: List[int], quantity: List[int]) -> bool:
        count = collections.Counter(nums)
        left = sorted(count.values(), reverse=True)
        quantity.sort(reverse=True)
        
        return self.helper(left, quantity, 0)
    
    def helper(self, left, quantity, cur):
        if cur == len(quantity):
            return True
        
        for i in range(len(left)):
            if left[i] >= quantity[cur]:
                left[i] -= quantity[cur]
                if self.helper(left, quantity, cur + 1):
                    return True
                left[i] += quantity[cur]
        return False