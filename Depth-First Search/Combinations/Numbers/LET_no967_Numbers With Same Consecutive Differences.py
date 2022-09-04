class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        res = []
        for i in range(9, 0, -1):
            self.dfs(i, n - 1, k, [i], res)
        return res
    
    def dfs(self, cur, remain, diff, temp, res):
        if remain == 0:
            num = 0
            for d in temp:
                num = num * 10 + d
            res.append(num)
            return
        
        if 0 <= cur + diff <= 9:
            temp.append(cur + diff)
            self.dfs(cur + diff, remain - 1, diff, temp, res)
            temp.pop()
        if diff == 0:
            return
        if 0 <= cur - diff <= 9:
            temp.append(cur - diff)
            self.dfs(cur - diff, remain - 1, diff, temp, res)
            temp.pop()

class Solution2:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        cur = set([i for i in range(1, 10)])
        for _ in range(n - 1):
            nxt = set()
            for num in cur:
                d = num % 10
                if 0 <= d + k <= 9:
                    nxt.add(num * 10 + (d + k))
                if 0 <= d - k <= 9:
                    nxt.add(num * 10 + (d - k))
            cur = nxt
        
        return list(cur)