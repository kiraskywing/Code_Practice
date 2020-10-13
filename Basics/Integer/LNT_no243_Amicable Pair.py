class Solution:
    """
    @param: k: An integer
    @return: all amicable pairs
    """
    def amicablePair(self, k):

        res = []
        temp = set()

        for i in range(1, k + 1):
            if i not in temp:
                x = self.converter(i)
                if x != i and x <= k and self.converter(x) == i:
                    res.append([i, x])
                    temp.update([i, x])

        return res

    def converter(self, k):

        tmp = 1

        for i in range(2, int(k ** 0.5) + 1):
            if k % i == 0:
                tmp += i + k // i

        return tmp