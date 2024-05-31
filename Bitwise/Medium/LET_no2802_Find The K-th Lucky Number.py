class Solution:
    def kthLuckyNumber(self, k: int) -> str:
        k += 1
        res = []
        while k != 1:
            res.append('7' if k & 1 else '4')
            k //= 2
        
        res.reverse()
        return ''.join(res)
