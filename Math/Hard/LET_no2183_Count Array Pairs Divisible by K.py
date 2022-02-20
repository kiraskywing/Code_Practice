class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        memo = collections.defaultdict(int)
        res = 0
        for num in nums:
            cur = self.gcd(num, k)
            for key, val in memo.items():
                if key * cur % k == 0:
                    res += val
            memo[cur] += 1
        return res
            
    def gcd(self, num, k):
        while k > 0:
            num, k = k, num % k
        return num