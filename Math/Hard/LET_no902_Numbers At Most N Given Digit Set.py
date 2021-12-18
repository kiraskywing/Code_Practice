class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        target = str(n)
        targetSize, dSize = len(target), len(digits)
        res = 0
        
        for i in range(1, targetSize):
            res += dSize ** i
        
        for i in range(targetSize):
            hasSame = False
            for d in digits:
                if d < target[i]:
                    res += dSize ** (targetSize - i - 1)
                elif d == target[i]:
                    hasSame = True
            if not hasSame:
                return res
        
        return res + 1