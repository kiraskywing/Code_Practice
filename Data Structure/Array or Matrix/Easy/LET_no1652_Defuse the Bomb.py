class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        if k < 0: 
            return self.decrypt(code[::-1], -k)[::-1]
        
        n = len(code)
        prefix = code * 2
        for i in range(n * 2):
            prefix[i] += i > 0 and prefix[i - 1]
            if k <= i < n + k:
                code[i - k] = prefix[i] - prefix[i - k]
        
        return code