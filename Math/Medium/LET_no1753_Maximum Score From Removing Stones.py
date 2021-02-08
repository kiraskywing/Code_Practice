class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        # solution 1
        temp = [a, b, c]
        temp.sort()
        res = 0
        while temp[1] > 0:
            res += 1
            temp[2] -= 1
            temp[1] -= 1
            temp.sort()
        
        return res

        # solution 2
        return min((a + b + c) // 2, a + b + c - max(a, b, c))
        # If all 3 nums become 0, then result is (a+b+c)/2
        # if 2 out of 3 are 0, it has to be sum of the minimum and middle one, so sum - max