class Solution:
    def nextGreaterElement(self, n: int) -> int:
        digits = list(str(n))
        for i in range(len(digits) - 2, -1, -1):
            if digits[i] < digits[i + 1]:
                for j in range(len(digits) - 1, i, -1):
                    if digits[j] > digits[i]:
                        digits[i], digits[j] = digits[j], digits[i]
                        digits[i + 1:] = sorted(digits[i + 1:])
                        res = int(''.join(digits))
                        return res if res < 1 << 31 else -1
        
        return -1