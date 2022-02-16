class Solution:
    """
    @param n: An integer
    @param str: a string with number from 1-n in random order and miss one number
    @return: An integer
    """
    def findMissing2(self, n, str):
        used = [False for _ in range(n + 1)]
        digits = 1 if n < 10 else 2
        return self.helper(str, 0, used, 0, n, digits)

    def helper(self, s, i, used, count, n, digits):
        if i == len(s) and count == n - 1:
            for j in range(1, n + 1):
                if not used[j]:
                    return j
        
        if i >= len(s) or s[i] == '0':
            return 0
        
        for L in range(1, digits + 1):
            cur = int(s[i:i+L])
            if cur <= n and not used[cur]:
                used[cur] = True
                res = self.helper(s, i + L, used, count + 1, n, digits)
                if res > 0:
                    return res
                used[cur] = False
        
        return 0

