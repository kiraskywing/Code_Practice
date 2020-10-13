class Solution:
    """
    @param n: An integer
    @return: a list of combination
    """

    def getFactors(self, n):
        result = []
        self.helper(n, 2, [], result)
        return result

    def helper(self, num, start_fac, item, result):
        if num == 1:
            if len(item) > 1:
                result.append(item[:])
                return

        for i in range(start_fac, int(num ** 0.5) + 1):
            if num % i == 0:
                item.append(i)
                self.helper(num // i, i, item, result)
                item.pop()

        if num >= start_fac:
            item.append(num)
            self.helper(1, num, item, result)
            item.pop()
