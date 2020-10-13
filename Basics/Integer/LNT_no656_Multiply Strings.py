class Solution:
    """
    @param num1: a non-negative integers
    @param num2: a non-negative integers
    @return: return product of num1 and num2
    """
    def multiply(self, num1, num2):
        a = 0
        for i in num1:
            a = a * 10 + int(i)
        b = 0
        for j in num2:
            b = b * 10 + int(j)
        return str(a * b)
