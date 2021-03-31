class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        if not envelopes:
            return 0
        
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        res = []
        
        for i, env in enumerate(envelopes):
            idx = self.helper(res, envelopes, env[1])
            if idx == len(res) - 1:
                if res and envelopes[res[-1]][1] >= env[1]:
                    res[-1] = i
                else:
                    res.append(i)
            else:
                res[idx] = i
        
        return len(res)
            
    def helper(self, res, envs, target):
        left, right = 0, len(res) - 1
        
        while left + 1 < right:
            mid = (left + right) // 2
            if envs[res[mid]][1] >= target:
                right = mid
            else:
                left = mid
        
        if res and envs[res[left]][1] >= target:
            return left
        return right