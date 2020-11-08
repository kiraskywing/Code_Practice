class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        max_val = max(instructions)
        rec = [0] * (max_val + 1)
        mod = 10 ** 9 + 7
        
        res = 0
        for i, n in enumerate(instructions):
            res += min(self.get(rec, n - 1), i - self.get(rec, n))
            self.update(rec, n, max_val)
        
        return res % mod
        
    def update(self, rec, num, max_val):
        while num <= max_val:
            rec[num] += 1
            num += num & -num
    
    def get(self, rec, num):
        res = 0
        while num > 0:
            res += rec[num]
            num -= num & -num
        return res