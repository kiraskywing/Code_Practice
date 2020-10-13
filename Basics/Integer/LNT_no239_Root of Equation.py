class Solution:
    """
    @param: a: parameter of the equation
    @param: b: parameter of the equation
    @param: c: parameter of the equation
    @return: a double array, contains at most two root
    """
    def rootOfEquation(self, a, b, c):
        if b ** 2 - 4 * a * c > 0:
            return sorted([((0 - b) + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a), ((0 - b) - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)])
        elif b ** 2 - 4 * a * c == 0:
            return [(0 - b) / (2 * a)]
        else:
            return []

if __name__ == '__main__':
    ans = Solution()
    print(ans.rootOfEquation(1, 8, 15))