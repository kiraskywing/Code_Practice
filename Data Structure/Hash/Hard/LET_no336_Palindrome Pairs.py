class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        memo = {w:i for i, w in enumerate(words)}
        res = []
        
        for i, w in enumerate(words):
            for j in range(len(w) + 1):
                prefix = w[:j]
                surfix = w[j:]
                
                if prefix == prefix[::-1]:
                    front = surfix[::-1]
                    if front in memo and memo[front] != i:
                        res.append([memo[front], i])
                    
                if surfix and surfix == surfix[::-1]:
                    tail = prefix[::-1]
                    if tail in memo and memo[tail] != i:
                        res.append([i, memo[tail]])
        
        return res