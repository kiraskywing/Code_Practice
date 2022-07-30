class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        memo2 = collections.defaultdict(int)
        for w in words2:
            temp = collections.Counter(w)
            for c, counts in temp.items():
                memo2[c] = max(memo2[c], counts)
        
        res = []
        for w in words1:
            memo = collections.Counter(w)
            if all(memo[c] >= counts for c, counts in memo2.items()):
                res.append(w)
                
        return res