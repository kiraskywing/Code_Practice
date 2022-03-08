class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        even_mid = ["11", "69", "88", "96", "00"]
        odd_mid = ["0", "1", "8"]
        if n == 1:
            return odd_mid
        if n == 2:
            return even_mid[:-1]
        
        if n % 2 == 1:
            pre, middle = self.findStrobogrammatic(n - 1), odd_mid
        else:
            pre, middle = self.findStrobogrammatic(n - 2), even_mid
        size = (n - 1) // 2
        return [p[:size] + s + p[size:] for s in middle for p in pre]

class Solution2:
    def findStrobogrammatic(self, n: int) -> List[str]:
        pairs = [('0', '0'), ('1', '1'), ('6', '9'), ('8', '8'), ('9', '6')]
        cur_length = n % 2
        res = ['0', '1', '8'] if cur_length == 1 else [""]
        
        while cur_length < n:
            cur_length += 2
            temp = []
            for cur in res:
                for c1, c2 in pairs:
                    if cur_length == n and c1 == '0':
                        continue
                    temp.append(c1 + cur + c2)
            res = temp
        
        return res