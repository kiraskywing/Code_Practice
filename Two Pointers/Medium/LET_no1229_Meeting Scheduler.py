class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        slots1.sort()
        slots2.sort()
        
        i, j, m, n = 0, 0, len(slots1), len(slots2)
        while i < m and j < n:
            start, end = max(slots1[i][0], slots2[j][0]), min(slots1[i][1], slots2[j][1])
            if end - start >= duration:
                return [start, start + duration]
            
            if slots1[i][1] < slots2[j][1]:
                i += 1
            else:
                j += 1
        
        return []