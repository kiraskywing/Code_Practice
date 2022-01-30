class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        temp = collections.defaultdict(int)
        res = 0
        
        for num in deliciousness:
            for i in range(22):
                res += temp[2 ** i - num]
            temp[num] += 1
        
        return res % (10 ** 9 + 7)