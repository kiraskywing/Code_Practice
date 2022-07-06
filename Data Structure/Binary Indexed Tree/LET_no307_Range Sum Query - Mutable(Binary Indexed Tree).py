class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = [0] * len(nums)
        self.bit = [0] * (len(nums) + 1)
        for i, num in enumerate(nums):
            self.update(i, num)

    def update(self, index: int, val: int) -> None:
        diff = val - self.nums[index]
        self.nums[index] = val
        
        index += 1
        while index <= len(self.nums):
            self.bit[index] += diff
            index += (index & -index)

    def sumRange(self, left: int, right: int) -> int:
        return self.query(right) - self.query(left - 1)
        
    def query(self, index):
        res = 0
        index += 1
        while index > 0:
            res += self.bit[index]
            index -= (index & -index)
        
        return res

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)