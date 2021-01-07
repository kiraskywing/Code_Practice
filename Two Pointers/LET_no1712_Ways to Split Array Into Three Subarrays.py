class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        prefix = [0]
        for x in nums: prefix.append(prefix[-1] + x)
        
        n = len(prefix)
        res = j = k = 0
        for i in range(1, n - 1):
            j = max(j, i + 1)
            while j < n - 1 and prefix[i] > prefix[j] - prefix[i]:
                j += 1
            k = max(k, j)
            while k < n - 1 and prefix[k] - prefix[i] <= prefix[-1] - prefix[k]:
                k += 1
            res += k - j
        
        return res % (10 ** 9 + 7)