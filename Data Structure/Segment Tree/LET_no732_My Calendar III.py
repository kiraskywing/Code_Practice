class Node:
    def __init__(self, start, end, times=1):
        self.start, self.end = start, end
        self.times = times
        self.left = self.right = None

class MyCalendarThree:

    def __init__(self):
        self.root = None
        self.counts = 0

    def book(self, start: int, end: int) -> int:
        self.root = self.insert(self.root, start, end, 1)
        return self.counts
        
    def insert(self, cur, start, end, times):
        if start >= end:
            return cur
        
        if not cur:
            self.counts = max(self.counts, times)
            return Node(start, end, times)
        
        if start >= cur.end:
            cur.right = self.insert(cur.right, start, end, times)
            return cur
        elif end <= cur.start:
            cur.left = self.insert(cur.left, start, end, times)
            return cur
        else:
            start1 = min(start, cur.start)
            end1 = max(start, cur.start)
            start2 = min(end, cur.end)
            end2 = max(end, cur.end)
            
            left_times = cur.times if start1 == cur.start else times
            right_times = cur.times if end2 == cur.end else times
            
            cur.left = self.insert(cur.left, start1, end1, left_times)
            cur.right = self.insert(cur.right, start2, end2, right_times)
            cur.times += times
            cur.start = end1
            cur.end = start2
            
            self.counts = max(self.counts, cur.times)
            
            return cur


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)