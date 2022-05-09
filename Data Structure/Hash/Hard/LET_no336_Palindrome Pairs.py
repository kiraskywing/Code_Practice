class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        memo = {w:i for i, w in enumerate(words)}
        res = []
        for index, w in enumerate(words):
            n = len(w)
            for i in range(n + 1):
                pre = w[:i]
                sur = w[i:]
                if pre == pre[::-1]:
                    front = sur[::-1]
                    if front in memo and memo[front] != index:
                        res.append([memo[front], index])
                if i != n and sur == sur[::-1]:
                    tail = pre[::-1]
                    if tail in memo and memo[tail] != index:
                        res.append([index, memo[tail]])
        
        return res