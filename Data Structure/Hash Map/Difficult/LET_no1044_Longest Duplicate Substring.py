class Solution:
    def longestDupSubstring(self, s: str) -> str:
        left, right = 0, len(s)
        res = ""
        while left + 1 < right:
            mid = (left + right) // 2
            found, candidate = self.robinKarp(s, mid)
            if found:
                res, left = candidate, mid
            else:
                right = mid
        return res
    
    def robinKarp(self, s, L):
        if L == 0:
            return True, ""
        
        mod, t, d, b = (1 << 31) - 1, 0, 256, 1
        for i in range(L - 1):
            b = b * d % mod
        
        dic = collections.defaultdict(list)
        for i in range(L):
            t = (t * d + ord(s[i])) % mod
        dic[t].append(i - L + 1)
        
        for i in range(len(s) - L):
            t = ((t - ord(s[i]) * b) * d + ord(s[i + L])) % mod
            for j in dic[t]:
                if s[i+1:i+1+L] == s[j:j+L]:
                    return True, s[j:j+L]
            dic[t].append(i + 1)
        
        return False, ""