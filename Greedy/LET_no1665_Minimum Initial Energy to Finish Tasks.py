class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key = lambda x : x[1] - x[0])
        res = 0
        
        for actual, minimum in tasks:
            res = max(res + actual, minimum)
        
        return res