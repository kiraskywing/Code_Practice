class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        arr = []
        extra = 0
        x0, y0 = location
        
        for x, y in points:
            if x == x0 and y == y0:
                extra += 1
                continue
            arr.append(math.atan2(y - y0, x - x0))
        
        arr.sort()
        arr = arr + [x + 2 * math.pi for x in arr]
        angle *= math.pi / 180
        
        left = ans = 0
        for right in range(len(arr)):
            while arr[right] - arr[left] > angle:
                left += 1
            ans = max(ans, right - left + 1)
        
        return ans + extra