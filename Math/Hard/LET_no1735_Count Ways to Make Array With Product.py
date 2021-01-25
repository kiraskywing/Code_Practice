class Solution:
    def waysToFillArray(self, queries: List[List[int]]) -> List[int]:
        res = []
        dp, fac = {}, {}
        for q in queries:
            if q[0] == 1 or q[1] == 1:
                res.append(1)
                continue
            
            w = self.ways(dp, fac, q[1])
            cur = 0
            for k, v in w.items():
                if k > q[0]:
                    continue
                cur = (cur + comb(q[0], k) * v) % (10 ** 9 + 7)
            res.append(cur)
        
        return res
    
    def ways(self, dp, fac, n):
        if n in dp: return dp[n]
        
        facs = self.factors(fac, n)
        if not facs:
            return {1 : 1}
        
        res = collections.defaultdict(int)
        res[1] = 1
        for f in facs:
            for k, v in self.ways(dp, fac, n // f).items():
                res[k + 1] += v
        dp[n] = res
        
        return dp[n]
    
    def factors(self, fac, n):
        if n in fac: return fac[n]
        
        res = []
        for i in range(2, n):
            if n % i == 0:
                res.append(i)
        fac[n] = res
        return fac[n]