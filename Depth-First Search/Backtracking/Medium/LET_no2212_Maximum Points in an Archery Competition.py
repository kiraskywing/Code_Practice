class Solution:
    def maximumBobPoints(self, numArrows: int, aliceArrows: List[int]) -> List[int]:
        memo = {}
        res = [0] * 12
        remain = numArrows
        for score in range(11, -1, -1):
            if self.dfs(remain, score, memo, aliceArrows) > self.dfs(remain, score - 1, memo, aliceArrows):
                res[score] = aliceArrows[score] + 1
                remain -= res[score]
        res[0] += remain
        return res
    
    def dfs(self, remain, score, memo, arrows):
        if score <= 0 or remain <= 0:
            return 0
        
        if (remain, score) in memo:
            return memo[(remain, score)]
        
        cur = self.dfs(remain, score - 1, memo, arrows)
        if remain > arrows[score]:
            cur = max(cur, self.dfs(remain - (arrows[score] + 1), score - 1, memo, arrows) + score)
        memo[(remain, score)] = cur    
        
        return memo[(remain, score)]