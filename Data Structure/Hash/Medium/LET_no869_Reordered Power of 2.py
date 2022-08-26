class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        memo = collections.Counter(str(n))
        for i in range(31):
            memo2 = collections.Counter(str(1 << i))
            if memo == memo2:
                return True
        
        return False