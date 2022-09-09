class HitCounter:

    def __init__(self):
        self.queue = collections.deque([])

    def hit(self, timestamp: int) -> None:
        self.queue.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        while self.queue and timestamp - self.queue[0] >= 300:
            self.queue.popleft()
        return len(self.queue)


class HitCounter2:

    def __init__(self):
        self.times = []
        self.counts = collections.defaultdict(int)
        self.diff = 300

    def hit(self, timestamp: int) -> None:
        if timestamp not in self.counts:
            self.counts[timestamp] = 1
            if self.times:
                self.counts[timestamp] += self.counts[self.times[-1]]
            self.times.append(timestamp)
        else:
            self.counts[timestamp] += 1

    def getHits(self, timestamp: int) -> int:
        if not self.times:
            return 0
        
        high = self.get_lower_counts(timestamp)
        low = self.get_lower_counts(timestamp - 300)
        return high - low
        
    def get_lower_counts(self, timestamp):
        left, right = 0, len(self.times) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if self.times[mid] >= timestamp:
                right = mid
            else:
                left = mid
        
        if self.times[right] <= timestamp:
            return self.counts[self.times[right]]
        if self.times[left] <= timestamp:
            return self.counts[self.times[left]]
        return 0


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)