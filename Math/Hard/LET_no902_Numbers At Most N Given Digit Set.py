class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        n = str(n)
        
        res = sum(len(digits) ** i for i in range(1, len(n)))
        
        i = 0
        while i < len(n):
            res += sum(d < n[i] for d in digits) * (len(digits) ** (len(n) - 1 - i))
            if n[i] not in digits:
                break
            i += 1
        
        return res + (i == len(n))