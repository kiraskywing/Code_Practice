class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        res = ['a'] * n
        k -= n
        
        i = n - 1
        while k > 0:
            cur = min(25, k)
            res[i] = chr(ord(res[i]) + cur)
            k -= cur
            i -= 1
        
        return ''.join(res)