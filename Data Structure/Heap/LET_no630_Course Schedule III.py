class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        heap = []
        total_time = 0
        
        for t, d_day in sorted(courses, key=lambda x: x[1]):
            total_time += t
            heapq.heappush(heap, -t)
            
            if total_time > d_day:
                total_time += heapq.heappop(heap)
        
        return len(heap)