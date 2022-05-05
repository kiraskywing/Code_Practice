class Solution:
    """
    @param n: Given a decimal number that is passed in as a string
    @return: A string
    """
    def binary_representation(self, n: str) -> str:
        int_part, frac_part = "", ""
        try:
            int_part, frac_part = n.split('.')
        except ValueError:
            int_part, frac_part = n, '0'
        
        if int(frac_part) % 5 != 0:
            return "ERROR"

        if int(frac_part) == 0:
            return self.helper(int_part)

        prac_count = 0
        res = []
        frac_part = float("0." + frac_part)
        while frac_part != 0.0:
            frac_part *= 2
            if frac_part >= 1:
                res.append('1')
                frac_part -= 1
            else:
                res.append('0')
            
            prac_count += 1
            if prac_count > 32:
                return "ERROR"
        
        return self.helper(int_part) + '.' + ''.join(res)

    def helper(self, num):
        num = int(num)
        if num == 0:
            return '0'
        
        res = []
        while num > 0:
            res.append(str(num % 2))
            num //= 2
        return ''.join(res)[::-1]