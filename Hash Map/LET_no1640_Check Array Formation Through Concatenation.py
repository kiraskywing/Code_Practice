class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        temp = {x[0]: x for x in pieces}
        res = []
        for n in arr:
            res += temp.get(n, [])
        
        return res == arr