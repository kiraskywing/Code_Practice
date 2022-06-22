class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        times = []
        for start, end in slots1 + slots2:
            if end - start >= duration:
                times.append((start, 1))
                times.append((end, -1))
        times.sort()
        
        start = end = None
        cur = 0
        i = 0
        while i < len(times):
            t, val = times[i]
            cur += val
            i += 1
            while i < len(times) and times[i][0] == t:
                cur += times[i][1]
                i += 1
            
            if cur == 2:
                start = t
            elif start is not None and cur <= 1:
                if t - start >= duration:
                    return [start, start + duration]
                start = None
        
        return []
                