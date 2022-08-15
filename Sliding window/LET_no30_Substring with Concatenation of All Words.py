class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        memo = collections.Counter(words)
        n = len(words)
        w_size = len(words[0])
        total_size = n * w_size
        m = len(s)
        
        if m < total_size:
            return []
        
        res = []
        for i in range(m - total_size + 1):
            memo2 = copy.deepcopy(memo)
            for j in range(i, i + total_size, w_size):
                w = s[j:j+w_size]
                memo2[w] -= 1
                if memo2[w] < 0:
                    break
            if all(val == 0 for val in memo2.values()):
                res.append(i)
        
        return res