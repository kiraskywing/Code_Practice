class Solution:
    def thousandSeparator(self, n: int) -> str:
        temp = []
        
        while n // 1000 > 0:
            temp.append(str(n)[-3:])
            n //= 1000
        temp.append(str(n))
        
        return ".".join(temp[::-1])