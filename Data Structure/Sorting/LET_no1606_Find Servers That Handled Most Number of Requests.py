class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        busy_jobs = []
        after = []
        before = [i for i in range(k)]
        request_times = [0] * k
        
        for i, (start, duration) in enumerate(zip(arrival, load)):
            server_id = i % k
            if server_id == 0:
                after = before
                before = []
            
            while busy_jobs and busy_jobs[0][0] <= start:
                free_node = heapq.heappop(busy_jobs)[1]
                if free_node < server_id:
                    heapq.heappush(before, free_node)
                else:
                    heapq.heappush(after, free_node)
            
            queue = after if after else before
            if not queue:
                continue
            using_node = heapq.heappop(queue)
            request_times[using_node] += 1
            heapq.heappush(busy_jobs, (start + duration, using_node))
        
        max_request = max(request_times)
        return [i for i in range(k) if request_times[i] == max_request]