class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        freq = [times for times in Counter(arr).values()]
        freq.sort()
        res, half = 0, len(arr) // 2
        while half > 0:
            half -= freq.pop()
            res += 1
            
        return res

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        memo = collections.Counter(arr)
        max_counts = max(memo.values())
        buckets_by_counts = [0] * (max_counts + 1)
        for counts in memo.values():
            buckets_by_counts[counts] += 1
            
        half_size = len(arr) // 2
        total = 0
        cur_counts = max_counts
        while half_size > 0:
            need = math.ceil(half_size / cur_counts)
            provide = min(buckets_by_counts[cur_counts], need)
            total += provide
            half_size -= provide * cur_counts
            cur_counts -= 1
        
        return total