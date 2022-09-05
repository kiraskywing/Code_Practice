class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        s_count = [collections.Counter(s) for s in stickers]
        memo = {'':0}
        return self.helper(''.join(sorted(target)), s_count, memo)
    
    def helper(self, target, s_count, memo):
        if target not in memo:
            t_count = collections.Counter(target)
            res = float('inf')
            
            for i in range(len(s_count)):
                if target[0] not in s_count[i]:
                    continue
                
                temp = []
                for c, n in t_count.items():
                    temp.append(c * (n - min(n, s_count[i][c])))
                sub_res = self.helper(''.join(temp), s_count, memo)
                if sub_res != -1:
                    res = min(res, 1 + sub_res)
            
            memo[target] = res if res != float('inf') else -1
        
        return memo[target]