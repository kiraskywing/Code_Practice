class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        res = []
        for num in nums:
            while res:
                x = math.gcd(res[-1], num)
                if x == 1:
                    break
                num *= res.pop() // x
            res.append(num)
        return res