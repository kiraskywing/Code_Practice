class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        freq = [times for times in Counter(arr).values()]
        freq.sort()
        res, half = 0, len(arr) // 2
        while half > 0:
            half -= freq.pop()
            res += 1
            
        return res