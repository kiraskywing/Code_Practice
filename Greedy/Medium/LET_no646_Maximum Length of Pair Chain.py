class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x : x[1])
        res = 0
        cur = float('-inf')
        for first, second in pairs:
            if first > cur:
                res += 1
                cur = second
        
        return res