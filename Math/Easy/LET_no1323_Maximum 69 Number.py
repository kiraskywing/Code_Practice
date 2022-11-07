class Solution:
    def maximum69Number (self, num: int) -> int:
        pos = 0
        res_i = -1
        temp = num
        
        while temp > 0:
            if temp % 10 == 6:
                res_i = pos
            
            temp //= 10
            pos += 1
        
        return num if res_i == -1 else num + 3 * (10 ** res_i)