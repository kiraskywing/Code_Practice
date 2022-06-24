class TimeMap:

    def __init__(self):
        self.memo = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.memo[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.memo:
            return ""
        
        return self.helper(self.memo[key], timestamp)
    
    def helper(self, arr, target):
        left, right = 0, len(arr) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if arr[mid][0] <= target:
                left = mid
            else:
                right = mid
        
        if arr[right][0] <= target:
            return arr[right][1]
        if arr[left][0] <= target:
            return arr[left][1]
        return ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)