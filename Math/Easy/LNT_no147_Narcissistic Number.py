class Solution:
    """
    @param n: The number of digits
    @return: All narcissistic numbers with n digits
    """
    def getNarcissisticNumbers(self, n):
        if n == 1:
            return [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        result = []
        for i in range(10 ** (n - 1), 10 ** n):
            temp = 0
            num = i
            while num > 0:
                temp += (num % 10) ** n
                num //= 10
            if i == temp:
                result.append(i)
        return result
